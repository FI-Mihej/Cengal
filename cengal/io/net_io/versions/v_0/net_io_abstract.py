#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import socket
import errno
import copy
import enum
from contextlib import contextmanager

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


class LoopIsAlreadyBegun(Exception):
    """
    You can not run NetIOUserApi.start() if it was already started (and still running).
    """
    pass


class WrongConnectionType(Exception):
    """
    You cannot run NetIOUserApi.make_connection() for ConnectionType.active_accepted connection. This kind of
    connections are made only from (and by) inside of IO loop and logic itself.
    """
    pass


class CanNotMakeConnection(Exception):
    """
    Currently not used. If there will be some exception on connect() call - it will be raised without any changes.
    """
    pass


class ConnectionType(enum.Enum):
    passive = 0  # passive socket (bind())
    active_accepted = 1  # active accepted socket (accept())
    active_connected = 2  # active connected socket (connect())


class ConnectionState(enum.Enum):
    not_connected_yet = 0  # socket is not in connection process
    waiting_for_connection = 1  # socket is in connection process (async connection is delayed)
    connected = 2  # socket is successfully connected
    worker_fault = 3  # there was unhandled exception from one of the WorkerBase callbacks
    io_fault = 4  # there was some IO trouble
    waiting_for_disconnection = 5  # connection was marked as "should be closed" but was not closed yet
    disconnected = 6  # socket is closed


class ConnectionInfo:
    def __init__(self,
                 worker_obj,
                 connection_type: ConnectionType,
                 socket_address=None,
                 socket_family=socket.AF_INET,
                 socket_type=socket.SOCK_STREAM,
                 socket_protocol=0,
                 socket_fileno=None,
                 backlog=0):
        """
        :param worker_obj: constructed worker object (see WorkerBase for more info). If this is a passive
            connection - it (worker_obj) will be inherited by the descendant active_accepted connections
            by copy.copy() call (see WorkerBase.__copy__() method for more info)
        :param connection_type: see ConnectionType() description
        :param socket_address:  see socket.bind()/socket.connect() docs
        :param socket_family: see socket.socket() docs
        :param socket_type: see socket.socket() docs
        :param socket_protocol: see socket.socket() docs
        :param socket_fileno: see socket.socket() docs
        :param backlog: see socket.listen() docs
        """
        self.worker_obj = worker_obj
        self.connection_type = connection_type
        self.socket_address = socket_address
        self.socket_family = socket_family
        self.socket_type = socket_type
        self.socket_protocol = socket_protocol
        self.socket_fileno = socket_fileno
        self.backlog = backlog


class Connection:
    """
    Connection class. Usually created by IO loop or by IO API. But you can also create it by yourself
    """
    def __init__(self,
                 connection_id,
                 connection_info: ConnectionInfo,
                 connection_and_address_pair: tuple,
                 connection_state: ConnectionState,
                 connection_name=None,
                 ):
        """
        :param connection_id: unique connection identificator (unique within the IO object). You may use some random
            GUID if you are creating connection by your self.
        :param connection_info: new connection will be created using information provided in connection_info object.
            See ConnectionInfo() for more information
        :param connection_and_address_pair: (conn, address) tuple where conn is connected socket (or it can be socket
            is in the process of connection. But only if it was made by IO loop.).
        :param connection_state: see ConnectionState for more information
        :param connection_name: name of the connection (if it was provided)
        """
        self.connection_id = connection_id
        self.connection_info = connection_info
        self.conn, self.address = connection_and_address_pair
        self.connection_state = connection_state
        self.connection_name = connection_name
        self.worker_obj = connection_info.worker_obj
        self.read_data = b''  # already read data
        self.must_be_written_data = memoryview(b'')  # this data should be written
        self.force_write_call = False

    def add_must_be_written_data(self, data):
        """
        Use this method to add data to output buffers
        :param data: some new output data to be send through this connection
        :return:
        """
        self.must_be_written_data = memoryview(bytes(self.must_be_written_data) + data)


class NetIOUserApi:
    """
    You may rely and use freely use methods of this base class from inside your program or from inside your worker
    (WorkerBase).
    """
    def __init__(self):
        super().__init__()
        self.all_connections = set()
        self.passive_connections = set()

        self.connection_by_id = dict()
        self.connection_by_name = dict()
        self.connection_by_fileno = dict()

    def start(self, destroy_on_finish=True):
        """
        Will start IO loop
        :param destroy_on_finish: if True - destroy() will be called from inside of this method
        :return:
        """
        raise NotImplementedError()

    def stop(self):
        """
        Will initiate IO loop stop process
        :return:
        """
        raise NotImplementedError()

    def make_connection(self, connection_info: ConnectionInfo = None, name=None)->Connection:
        """
        Will create connection from given connection_info object. Than connection will be established. Immediate or
        delayed - depends on the connection type:
        - ConnectionType.passive - immediate;
        - ConnectionType.active_connected - delayed.
        In both cases WorkerBase.on_connect will be called immediately after connection will be successfully
        established (IF it will be successfully established).
        :param connection_info: new connection will be created using information provided in connection_info object.
            See ConnectionInfo() for more information
        :param name: name of the connection. If you'll provide it - you will be able to find this connection in
            NetIOUserApi.connection_by_name dictionary by it's name.
        :return:
        """
        raise NotImplementedError()

    def add_connection(self, connection: Connection):
        """
        Will register already established connection. You need to use this method for example if you have already
        connected socket
        :param connection:
        :return:
        """
        raise NotImplementedError()

    def remove_connection(self, connection: Connection):
        """
        Will close and remove connection
        :param connection:
        :return:
        """
        raise NotImplementedError()

    def check_is_connection_need_to_sent_data(self, connection: Connection):
        """
        Will check connection to output data presence. It is automatically called after EACH WorkerBase callback call
        by the IO loop. But if you are filling other connection's output buffer - you'll need to make this call for that
        connection by your self.
        :param connection:
        :return:
        """
        raise NotImplementedError()


class NetIOCallbacks:
    """
    Callbacks from this class will be called from inside (and by) IOMethodBase loop.
    """
    def __init__(self):
        super().__init__()

    def on_accept_connection(self, connection: Connection):
        raise NotImplementedError()

    def on_connected(self, connection: Connection):
        raise NotImplementedError()

    def on_read(self, connection: Connection):
        raise NotImplementedError()

    def on_write(self, connection: Connection):
        raise NotImplementedError()

    def on_close(self, connection: Connection):
        raise NotImplementedError()


class NetIOBase(NetIOUserApi, NetIOCallbacks):
    """
    Base class for any IO implementation (Linux, BSD, Windows, cross platform, etc.).
    """
    def __init__(self, transport):
        """

        :param transport: class of the desired IOMethod. Instance (object) will be created by NetIOBase itself
        """
        super().__init__()
        self.method = transport(self)

    def destroy(self):
        raise NotImplementedError()


class WorkerBase:
    """
    Base class for all workers.
    on_* callbacks will be called by the IO loop.

    General info:
    You can read input data from self.connection at any time (see "Caution" section of __init__ doc string) from any
    callback.
    You can write output data (to be send) to self.connection at any time (see "Caution") from any callback.
    """
    def __init__(self, api: NetIOUserApi=None, connection: Connection=None):
        """
        Caution:
        Please do not rely on self.api and self.connection inside of your __init__ constructor: it is guaranteed that
        they will be set before any callback call, but not at the construction process.

        :param api: link to the constructed network io object
        :param connection: link to the constructed connection object
        """
        self.api = api
        self.connection = connection

    def on_connect(self):
        """
        Will be called after connection successfully established
        :return:
        """
        pass

    def on_read(self):
        """
        Will be called if there is some NEW data in the connection input buffer
        :return:
        """
        pass

    def on_no_more_data_to_write(self):
        """
        Will be called after all data is sent.
        Normally it will be called once (one single shot after each portion of out data is sent).
        If you'll set self.connection.force_write_call to True state - this callback may be called continuously
        (but not guaranteed: it depends of used IOMethod implementation)
        :return:
        """
        pass

    def on_connection_lost(self):
        """
        Will be called AFTER connection socket was actually closed and removed from IOMethod checking list.
        At this time, self.connection.connection_state is already set to ConnectionState.disconnected.
        :return:
        """
        pass

    def __copy__(self):
        """
        This method SHOULD be implemented. It should create a new instance and copy some global (shared) data from
        current object to that new instance. It will be called when new peer is connected to existing passive connection
        So this is the way you may use to give all new connection some links to some global data by worker object of
        the passive connection replication process.
        :return:
        """
        raise NotImplementedError()


@contextmanager
def net_io(net_io_obj: NetIOBase):
    """
    Context manager.
    Usage:

    main_io = NetIOBase()
    with(net_io(main_io)) as io:
        print('Preparing connections')
        connection1 = io.make_connection(...)
        connection2 = io.make_connection(...)
        k = c + 12
        ...
        connectionN = io.make_connection(...)
        print('Starting IO loop')
    print('IO loop was finished properly')


    :param net_io_obj: constructed IO instance (object)
    :return:
    """
    try:
        yield net_io_obj
        net_io_obj.start(destroy_on_finish=False)
    finally:
        net_io_obj.destroy()


class IOMethodBase:
    """
    Base class for all IOMethod implementation (select, epoll, overlapped io, kqueue, etc.)
    All his methods are called by the NetIOBase instance.
    """
    def __init__(self, interface: NetIOBase):
        self.interface = interface
        self.should_be_closed = set()
        pass

    def loop_iteration(self, timeout=None):
        """
        Single IO loop iteration.
        This method holds all IOMethod logic.
        :return:
        """
        raise NotImplementedError()

    def destroy(self):
        """
        Initiates destruction process
        :return:
        """
        raise NotImplementedError()

    def set__can_read(self, conn: socket.socket, state=True):
        """
        Will allow (True) or disallow (False) "socket available to read" checks for socket
        :param conn: target socket
        :param state: True - allow; False - disallow
        :return:
        """
        raise NotImplementedError()

    def set__need_write(self, conn: socket.socket, state=True):
        """
        Will allow (True) or disallow (False) "socket available to write" checks for socket
        :param conn: target socket
        :param state: True - allow; False - disallow
        :return:
        """
        raise NotImplementedError()

    def set__should_be_closed(self, conn: socket.socket):
        """
        Mark socket as "should be closed"
        :param conn: target socket
        :return:
        """
        raise NotImplementedError()

    def add_connection(self, conn: socket.socket):
        """
        Will add socket to the internal connections list
        :param conn: target socket
        :return:
        """
        raise NotImplementedError()

    def remove_connection(self, conn: socket.socket):
        """
        Will remove socket from the internal connections list
        :param conn: target socket
        :return:
        """
        raise NotImplementedError()
