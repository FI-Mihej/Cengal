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


__all__ = ['StreamManagerAbstract', 'StreamReaderAbstract', 'StreamReaderProtocolAbstract', 'StreamWriterAbstract']


from typing import Tuple, Set, Optional, Union
from .efficient_streams_base_internal import *
from .efficient_streams_base import *


class StreamManagerAbstract:
    def __init__(self) -> None:
        raise NotImplementedError

    async def open_connection(self, host=None, port=None, *,
                            loop=None, limit=DEFAULT_LIMIT,
                            stream_type: StreamType = StreamType.general, stream_name: str = str(),
                            protocol_greeting: Optional[str] = None, message_size_len: Optional[int] = None,
                            max_message_size_len: Optional[int] = None,
                            **kwds) -> Tuple['StreamReaderAbstract', 'StreamWriterAbstract']:
        """A wrapper for create_connection() returning a (reader, writer) pair.

        The reader returned is a StreamReaderAbstract instance; the writer is a
        StreamWriterAbstract instance.

        The arguments are all the usual arguments to create_connection()
        except protocol_factory; most common are positional host and port,
        with various optional keyword arguments following.

        Additional optional keyword arguments are loop (to set the event loop
        instance to use) and limit (to set the buffer limit passed to the
        StreamReaderAbstract).

        (If you want to customize the StreamReaderAbstract and/or
        StreamReaderProtocolAbstract classes, just copy the code -- there's
        really nothing special here except some convenience.)
        """
        raise NotImplementedError

    async def start_server(self, client_connected_cb, host=None, port=None, *,
                        loop=None, limit=DEFAULT_LIMIT,
                        stream_type: StreamType = StreamType.general, stream_name: str = str(),
                        gate_security_policy: GateSecurityPolicy = GateSecurityPolicy.disabled, policy_managed_stream_names: Optional[Set[str]] = None,
                        protocol_greeting: Optional[str] = None, message_size_len: Optional[int] = None,
                        max_message_size_len: Optional[int] = None,
                        **kwds):
        """Start a socket server, call back for each client connected.

        The first parameter, `client_connected_cb`, takes two parameters:
        client_reader, client_writer.  client_reader is a StreamReaderAbstract
        object, while client_writer is a StreamWriterAbstract object.  This
        parameter can either be a plain callback function or a coroutine;
        if it is a coroutine, it will be automatically converted into a
        Task.

        The rest of the arguments are all the usual arguments to
        loop.create_server() except protocol_factory; most common are
        positional host and port, with various optional keyword arguments
        following.  The return value is the same as loop.create_server().

        Additional optional keyword arguments are loop (to set the event loop
        instance to use) and limit (to set the buffer limit passed to the
        StreamReaderAbstract).

        The return value is the same as loop.create_server(), i.e. a
        Server object which can be used to stop the service.
        """
        raise NotImplementedError

    async def try_establish_message_protocol_server_side(self, reader: 'StreamReaderAbstract', writer: 'StreamWriterAbstract') -> bool:
        raise NotImplementedError
    
    async def try_establish_message_protocol_client_side(self, reader: 'StreamReaderAbstract', writer: 'StreamWriterAbstract') -> bool:
        raise NotImplementedError


class StreamReaderAbstract:
    def __init__(self, manager: StreamManagerAbstract, message_protocol_settings: MessageProtocolSettings, *args, **kwargs) -> None:
        raise NotImplementedError
    
    async def read_max(self):
        raise NotImplementedError
    
    async def read_nearly_max(self):
        raise NotImplementedError
    
    async def read_with_counter(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    def at_eof(self):
        raise NotImplementedError

    async def readline(self):
        """Read chunk of data from the stream until newline (b'\n') is found.

        On success, return chunk that ends with newline. If only partial
        line can be read due to EOF, return incomplete line without
        terminating newline. When EOF was reached while no bytes read, empty
        bytes object is returned.

        If limit is reached, ValueError will be raised. In that case, if
        newline was found, complete line including newline will be removed
        from internal buffer. Else, internal buffer will be cleared. Limit is
        compared against part of the line without newline.

        If stream was paused, this function will automatically resume it if
        needed.
        """
        raise NotImplementedError

    async def readuntil(self, separator=b'\n'):
        """Read data from the stream until ``separator`` is found.

        On success, the data and separator will be removed from the
        internal buffer (consumed). Returned data will include the
        separator at the end.

        Configured stream limit is used to check result. Limit sets the
        maximal length of data that can be returned, not counting the
        separator.

        If an EOF occurs and the complete separator is still not found,
        an IncompleteReadError exception will be raised, and the internal
        buffer will be reset.  The IncompleteReadError.partial attribute
        may contain the separator partially.

        If the data cannot be read because of over limit, a
        LimitOverrunError exception  will be raised, and the data
        will be left in the internal buffer, so it can be read again.
        """
        raise NotImplementedError

    async def read(self, n=-1):
        """Read up to `n` bytes from the stream.

        If n is not provided, or set to -1, read until EOF and return all read
        bytes. If the EOF was received and the internal buffer is empty, return
        an empty bytes object.

        If n is zero, return empty bytes object immediately.

        If n is positive, this function try to read `n` bytes, and may return
        less or equal bytes than requested, but at least one byte. If EOF was
        received before any byte is read, this function returns empty byte
        object.

        Returned value is not limited with limit, configured at stream
        creation.

        If stream was paused, this function will automatically resume it if
        needed.
        """
        raise NotImplementedError

    async def read_nearly(self, n=-1):
        """Read up to `n` bytes from the stream.

        If n is not provided, or set to -1, read until EOF and return all read
        bytes. If the EOF was received and the internal buffer is empty, return
        an empty bytes object.

        If n is zero, return empty bytes object immediately.

        If n is positive, this function try to read `n` bytes, and may return
        less or equal bytes than requested, but at least one byte. If EOF was
        received before any byte is read, this function returns empty byte
        object.

        Returned value is not limited with limit, configured at stream
        creation.

        If stream was paused, this function will automatically resume it if
        needed.
        """
        raise NotImplementedError

    async def readexactly(self, n):
        """Read exactly `n` bytes.

        Raise an IncompleteReadError if EOF is reached before `n` bytes can be
        read. The IncompleteReadError.partial attribute of the exception will
        contain the partial read bytes.

        if n is zero, return empty bytes object.

        Returned value is not limited with limit, configured at stream
        creation.

        If stream was paused, this function will automatically resume it if
        needed.
        """
        raise NotImplementedError
    
    async def readonly_exactly(self, n):
        raise NotImplementedError
    
    async def read_message(self):
        raise NotImplementedError
    
    def message_awailable(self) -> bool:
        raise NotImplementedError
    
    def transport_pause_reading(self):
        raise NotImplementedError
    
    def transport_resume_reading(self):
        raise NotImplementedError


class StreamReaderProtocolAbstract:
    def __init__(self, manager: StreamManagerAbstract, message_protocol_settings: MessageProtocolSettings, *args, **kwargs) -> None:
        raise NotImplementedError

    def connection_made(self, transport):
        raise NotImplementedError


class StreamWriterAbstract:
    def __init__(self, *args, **kwargs) -> None:
        raise NotImplementedError

    def optimized_write(self, data):
        raise NotImplementedError

    def owrite(self, data):
        raise NotImplementedError

    async def partial_drain(self):
        raise NotImplementedError

    async def pdrain(self):
        return await self.partial_drain()

    async def full_drain(self):
        raise NotImplementedError

    async def fdrain(self):
        return await self.full_drain()
    
    def _release_autonomous_writer_waiters(self):
        raise NotImplementedError
    
    async def _autonomous_writer_impl(self):
        raise NotImplementedError
    
    def start_autonomous_writer(self):
        raise NotImplementedError
    
    def start_aw(self):
        return self.start_autonomous_writer()
    
    async def stop_autonomous_writer(self, timeout: Optional[Union[int, float]] = 0):
        """_summary_

        Args:
            timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout

        Returns:
            _type_: _description_
        """
        raise NotImplementedError
    
    def stop_ar(self, timeout: Optional[Union[int, float]] = 0):
        """_summary_

        Args:
            timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout

        Returns:
            _type_: _description_
        """
        return self.stop_autonomous_writer(timeout)
    
    async def autonomous_writer_drain_enough(self, lower_water_size: Optional[int] = None):
        raise NotImplementedError
    
    async def ar_drain_enough(self):
        await self.autonomous_writer_drain_enough()
    
    def optimized_write_message(self, data):
        raise NotImplementedError
    
    def owrite_message(self, data):
        self.optimized_write_message(data)
    
    async def send_message(self, data):
        raise NotImplementedError
