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


__all__ = ['StreamType', 'GateSecurityPolicy', 'StreamManagerIOCoreMemoryManagement', 'TcpStreamManager', 'TcpStreamReader', 'TcpStreamReaderProtocol', 'TcpStreamWriter']


import warnings
import asyncio
from asyncio.exceptions import IncompleteReadError, LimitOverrunError
from asyncio import streams
from asyncio.streams import StreamWriter as OriginalStreamWriter
from asyncio.streams import StreamReader as OriginalStreamReader
from asyncio.streams import StreamReaderProtocol as OriginalStreamReaderProtocol
from asyncio.sslproto import SSLProtocol, _SSLProtocolTransport
from asyncio.proactor_events import _ProactorSocketTransport
from asyncio.selector_events import _SelectorSocketTransport
from asyncio import events
from asyncio import proactor_events
from asyncio import selector_events
try:
    from asyncio import unix_events
except ImportError:
    pass

from asyncio import coroutines
from asyncio.tasks import sleep, Task
from asyncio.futures import Future
from copy import copy
from enum import Enum
from cengal.io.asock_io.versions.v_1.recv_buff_size_computer.recv_buff_size_computer__python import RecvBuffSizeComputer
# from cengal.io.asock_io.versions.v_1.base import IOCoreMemoryManagement
from cengal.parallel_execution.asyncio.atasks import create_task
from cengal.parallel_execution.asyncio.timed_yield import TimedYield
from cengal.hardware.info.cpu.versions.v_1 import CpuInfo
# from cengal.data_containers.dynamic_list_of_pieces import DynamicListOfPiecesDequeWithLengthControl
# from cengal.data_containers.fast_fifo import FIFODequeWithLengthControl, FIFOIsEmpty
# from cengal.data_manipulation.front_triggerable_variable import FrontTriggerableVariable, FrontTriggerableVariableType
from cengal.data_containers.dynamic_list_of_pieces.versions.v_1.dynamic_list_of_pieces__python import DynamicListOfPiecesDequeWithLengthControl
from cengal.code_flow_control.smart_values.versions import ValueExistence
from cengal.data_manipulation.conversion.reinterpret_cast import reinterpret_cast
from typing import Sequence, Tuple, Type, Set, Optional, Union, List, cast
from .efficient_streams_base_internal import *
from .efficient_streams_base import *
from .efficient_streams_abstract import *


class TcpStreamManager(StreamManagerAbstract):
    def __init__(self) -> None:
        self.io_memory_management: StreamManagerIOCoreMemoryManagement = StreamManagerIOCoreMemoryManagement()
        self.autonomous_writer_stop_default_timeout: Optional[Union[int, float]] = 10.0
        self.output_to_client_container_type = DynamicListOfPiecesDequeWithLengthControl
        self.input_from_client_container_type = DynamicListOfPiecesDequeWithLengthControl

    async def open_connection(self, host=None, port=None, *,
                            loop=None, limit=DEFAULT_LIMIT,
                            stream_type: StreamType = StreamType.general, stream_name: str = str(),
                            protocol_greeting: Optional[str] = None, message_size_len: Optional[int] = None,
                            max_message_size_len: Optional[int] = None,
                            **kwds) -> Tuple['TcpStreamReader', 'TcpStreamWriter']:
        """A wrapper for create_connection() returning a (reader, writer) pair.

        The reader returned is a TcpStreamReader instance; the writer is a
        TcpStreamWriter instance.

        The arguments are all the usual arguments to create_connection()
        except protocol_factory; most common are positional host and port,
        with various optional keyword arguments following.

        Additional optional keyword arguments are loop (to set the event loop
        instance to use) and limit (to set the buffer limit passed to the
        TcpStreamReader).

        (If you want to customize the TcpStreamReader and/or
        TcpStreamReaderProtocol classes, just copy the code -- there's
        really nothing special here except some convenience.)
        """
        if StreamType.gate == stream_type:
            raise ValueError(f'Wrong stream_type value: client can not be a "gate".')
        
        if loop is None:
            loop = events.get_event_loop()
        else:
            warnings.warn("The loop argument is deprecated since Python 3.8, "
                        "and scheduled for removal in Python 3.10.",
                        DeprecationWarning, stacklevel=2)
        
        message_protocol_settings: MessageProtocolSettings = MessageProtocolSettings(protocol_greeting, message_size_len, max_message_size_len)
        reader = TcpStreamReader(self, message_protocol_settings, limit=limit, loop=loop)
        protocol = TcpStreamReaderProtocol(self, message_protocol_settings, reader, loop=loop)
        transport, _ = await loop.create_connection(
            lambda: protocol, host, port, **kwds)
        writer = TcpStreamWriter(transport, protocol, reader, loop)
        return reader, writer
    
    def bind_existing_connection(self, reader: OriginalStreamReader, writer: OriginalStreamWriter, *, loop=None, limit=DEFAULT_LIMIT,
                            stream_type: StreamType = StreamType.general, stream_name: str = str(),
                            protocol_greeting: Optional[str] = None, message_size_len: Optional[int] = None,
                            max_message_size_len: Optional[int] = None,
                            **kwds) -> Tuple['TcpStreamReader', 'TcpStreamWriter']:
        reader = reinterpret_cast(TcpStreamReader, reader)
        message_protocol_settings: MessageProtocolSettings = MessageProtocolSettings(protocol_greeting, message_size_len, max_message_size_len)
        reader._bind_to_stream_manager(self, message_protocol_settings, limit=limit, loop=loop)
        
        protocol = reinterpret_cast(TcpStreamReaderProtocol, writer._protocol)
        protocol._bind_to_stream_manager(message_protocol_settings, reader, loop=loop)
        
        transport = writer._transport
        if isinstance(transport, _SSLProtocolTransport):
            transport = cast(_SSLProtocolTransport, transport)
            ssl_protocol: SSLProtocol = transport._ssl_protocol
            ssl_protocol._set_app_protocol(protocol)
        elif isinstance(transport, _ProactorSocketTransport):
            transport = cast(_ProactorSocketTransport, transport)
            transport.set_protocol(protocol)
        elif isinstance(transport, _SelectorSocketTransport):
            transport = cast(_SelectorSocketTransport, transport)
            transport.set_protocol(protocol)
        else:
            raise RuntimeError(f'Unsupported transport type: {type(transport)}')

        writer = reinterpret_cast(TcpStreamWriter, writer)
        writer._bind_to_stream_manager(self, transport, protocol, reader, loop)

        return reader, writer

    async def start_server(self, client_connected_cb, host=None, port=None, *,
                        loop=None, limit=DEFAULT_LIMIT,
                        stream_type: StreamType = StreamType.general, stream_name: str = str(),
                        gate_security_policy: GateSecurityPolicy = GateSecurityPolicy.disabled, policy_managed_stream_names: Optional[Set[str]] = None,
                        protocol_greeting: Optional[str] = None, message_size_len: Optional[int] = None,
                        max_message_size_len: Optional[int] = None,
                        **kwds):
        """Start a socket server, call back for each client connected.

        The first parameter, `client_connected_cb`, takes two parameters:
        client_reader, client_writer.  client_reader is a TcpStreamReader
        object, while client_writer is a TcpStreamWriter object.  This
        parameter can either be a plain callback function or a coroutine;
        if it is a coroutine, it will be automatically converted into a
        Task.

        The rest of the arguments are all the usual arguments to
        loop.create_server() except protocol_factory; most common are
        positional host and port, with various optional keyword arguments
        following.  The return value is the same as loop.create_server().

        Additional optional keyword arguments are loop (to set the event loop
        instance to use) and limit (to set the buffer limit passed to the
        TcpStreamReader).

        The return value is the same as loop.create_server(), i.e. a
        Server object which can be used to stop the service.
        """
        if loop is None:
            loop = events.get_event_loop()
        else:
            warnings.warn("The loop argument is deprecated since Python 3.8, "
                        "and scheduled for removal in Python 3.10.",
                        DeprecationWarning, stacklevel=2)

        def factory():
            message_protocol_settings: MessageProtocolSettings = MessageProtocolSettings(protocol_greeting, message_size_len, max_message_size_len)
            reader =  TcpStreamReader(self, message_protocol_settings, limit=limit, loop=loop)
            protocol = TcpStreamReaderProtocol(self, message_protocol_settings, reader, client_connected_cb,
                                            loop=loop)
            return protocol

        return await loop.create_server(factory, host, port, **kwds)

    def bind_accepted_connection(self, 
                            reader: OriginalStreamReader, writer: OriginalStreamWriter, *, loop=None, limit=DEFAULT_LIMIT,
                            stream_type: StreamType = StreamType.general, stream_name: str = str(),
                            protocol_greeting: Optional[str] = None, message_size_len: Optional[int] = None,
                            max_message_size_len: Optional[int] = None,
                            **kwds) -> Tuple['TcpStreamReader', 'TcpStreamWriter']:
        reader = reinterpret_cast(TcpStreamReader, reader)
        message_protocol_settings: MessageProtocolSettings = MessageProtocolSettings(protocol_greeting, message_size_len, max_message_size_len)
        reader._bind_to_stream_manager(self, message_protocol_settings, limit=limit, loop=loop)
        
        protocol = reinterpret_cast(TcpStreamReaderProtocol, writer._protocol)
        client_connected_cb = protocol._client_connected_cb
        protocol._bind_to_stream_manager(message_protocol_settings, reader, client_connected_cb, loop=loop)
        
        transport = writer._transport
        if isinstance(transport, _SSLProtocolTransport):
            transport = cast(_SSLProtocolTransport, transport)
            ssl_protocol: SSLProtocol = transport._ssl_protocol
            ssl_protocol._set_app_protocol(protocol)
        elif isinstance(transport, _ProactorSocketTransport):
            transport = cast(_ProactorSocketTransport, transport)
            transport.set_protocol(protocol)
        elif isinstance(transport, _SelectorSocketTransport):
            transport = cast(_SelectorSocketTransport, transport)
            transport.set_protocol(protocol)
        else:
            raise RuntimeError(f'Unsupported transport type: {type(transport)}')

        writer = reinterpret_cast(TcpStreamWriter, writer)
        writer._bind_to_stream_manager(self, transport, protocol, reader, loop)

        return reader, writer

    async def try_establish_message_protocol_server_side(self, reader: 'TcpStreamReader', writer: 'TcpStreamWriter') -> bool:
        message_size_len_encoded = await reader.readonly_exactly(1)
        message_size_len = int.from_bytes(message_size_len_encoded, 'little')
        can_be_established: bool = False
        if message_size_len <= reader._message_protocol_settings._max_message_size_len:
            message_size_encoded = await reader.readonly_exactly(message_size_len)
            message_size = int.from_bytes(message_size_encoded, 'little')
            message = await reader.readonly_exactly(message_size)
            if message == reader._message_protocol_settings._protocol_greeting:
                can_be_established = True
        
        if can_be_established:
            reader._message_protocol_settings._message_size_len = message_size_len
            writer._protocol._message_protocol_settings._message_size_len = message_size_len
            await reader.readexactly(1)
            await reader.read_message()
            message = len(reader._message_protocol_settings._message_size_len).to_bytes(1, 'little') + len(reader._message_protocol_settings._protocol_greeting).to_bytes(reader._message_protocol_settings._message_size_len, 'little') + reader._message_protocol_settings._protocol_greeting
            writer.write(message)
            await writer.full_drain()
            return True
        else:
            return False
    
    async def try_establish_message_protocol_client_side(self, reader: 'TcpStreamReader', writer: 'TcpStreamWriter') -> bool:
        message = len(reader._message_protocol_settings._message_size_len).to_bytes(1, 'little') + len(reader._message_protocol_settings._protocol_greeting).to_bytes(reader._message_protocol_settings._message_size_len, 'little') + reader._message_protocol_settings._protocol_greeting
        writer.write(message)
        await writer.full_drain()
        message_size_len_encoded = await reader.readonly_exactly(1)
        message_size_len = int.from_bytes(message_size_len_encoded, 'little')
        can_be_established: bool = False
        if message_size_len <= reader._message_protocol_settings._max_message_size_len:
            message_size_encoded = await reader.readonly_exactly(message_size_len)
            message_size = int.from_bytes(message_size_encoded, 'little')
            message = await reader.readonly_exactly(message_size)
            if message == reader._message_protocol_settings._protocol_greeting:
                can_be_established = True
        
        if can_be_established:
            reader._message_protocol_settings._message_size_len = message_size_len
            writer._protocol._message_protocol_settings._message_size_len = message_size_len
            await reader.readexactly(1)
            await reader.read_message()
            return True
        else:
            return False


# def classes_with_amax_size() -> Tuple[Type]:
#     types = list()
#     try:
#         pass
#     except AttributeError:
#         pass


# class StreamReaderCopy(OriginalStreamReader):
#     # def __init__(self, limit: int, loop: events.AbstractEventLoop) -> None:
#     #     self.stream_manager = None
#     #     super().__init__(limit, loop)
    
#     def __init__(self, manager: TcpStreamManager, original_stream_reader: OriginalStreamReader) -> None:
#         self._stream_manager = manager
#         self.recv_buff_size_computer = RecvBuffSizeComputer()
#         cpu_info = CpuInfo()
#         # self.recv_buff_size_computer.max_recv_buff_size = cpu_info.l3_cache_size
#         # self.recv_buff_size_computer.max_recv_buff_size = cpu_info.l2_cache_size_per_virtual_core
#         # self.recv_buff_size_computer.max_recv_buff_size = CpuInfo().l3_cache_size_per_virtual_core
#         # self.recv_buff_size_computer.max_recv_buff_size = 3145728
#         self.recv_buff_size_computer.max_recv_buff_size = 10 * 1024**2
#         # self.recv_buff_size_computer.max_recv_buff_size = 1024
#         print(f'max_recv_buff_size: {self.recv_buff_size_computer.max_recv_buff_size}')
#         original_dict: dict = copy(original_stream_reader.__dict__)
#         original_dict.pop('feed_data', None)
#         original_dict.pop('_stream_manager', None)
#         self.__dict__.update(original_dict)

#     def feed_data(self, data):
#         assert not self._eof, 'feed_data after feed_eof'

#         if not data:
#             return

#         data_len = len(data)
#         self.recv_buff_size_computer.calc_new_recv_buff_size(data_len)
#         self._buffer.extend(data)
#         self._wakeup_waiter()

#         if (self._transport is not None and
#                 not self._paused and
#                 len(self._buffer) > 2 * self._limit):
#             try:
#                 self._transport.pause_reading()
#             except NotImplementedError:
#                 # The transport can't be paused.
#                 # We'll just have to buffer all data.
#                 # Forget the transport so we don't keep trying.
#                 self._transport = None
#             else:
#                 self._paused = True

#     def _maybe_resume_transport(self):
#         if isinstance(self._transport, (
#             proactor_events._ProactorDatagramTransport,
#             selector_events._SelectorTransport,
#             unix_events._UnixReadPipeTransport
#             )):
#             # if hasattr(self._transport, 'max_size'):
#             try:
#                 self._transport.max_size = self.recv_buff_size_computer.recv_buff_size
#                 # print(f'max_size: {self._transport.max_size}')
#             except AttributeError:
#                 pass
#         else:
#             print(f'Unsupported transport: {type(self._transport)}')
        
#         if self._paused and len(self._buffer) <= self._limit:
#             self._paused = False
#             self._transport.resume_reading()
    
#     async def read_with_counter(self):
#         if self._exception is not None:
#             raise self._exception

#         # This used to just loop creating a new waiter hoping to
#         # collect everything in self._buffer, but that would
#         # deadlock if the subprocess sends more than self.limit
#         # bytes.  So just call self.read(self._limit) until EOF.
#         blocks = []
#         counter = 0
#         while True:
#             block = await self.read(self._limit)
#             counter += 1
#             if not block:
#                 break
#             blocks.append(block)
#         return b''.join(blocks), counter


class TcpStreamReader(OriginalStreamReader, StreamReaderAbstract):
    def __init__(self, manager: TcpStreamManager, message_protocol_settings: MessageProtocolSettings, *args, **kwargs) -> None:
        self._bind_to_stream_manager(manager, message_protocol_settings, *args, **kwargs)

    def _bind_to_stream_manager(self, manager: TcpStreamManager, message_protocol_settings: MessageProtocolSettings, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._stream_manager = manager
        self._message_protocol_settings: MessageProtocolSettings = message_protocol_settings
        self._smart_buffer: DynamicListOfPiecesDequeWithLengthControl = self._stream_manager.input_from_client_container_type(
            external_data_length=self._stream_manager.io_memory_management.global_in__data_full_size)
        self.recv_buff_size_computer = RecvBuffSizeComputer()
        cpu_info = CpuInfo()
        # self.recv_buff_size_computer.max_recv_buff_size = cpu_info.l3_cache_size
        # self.recv_buff_size_computer.max_recv_buff_size = cpu_info.l2_cache_size_per_virtual_core
        # self.recv_buff_size_computer.max_recv_buff_size = CpuInfo().l3_cache_size_per_virtual_core
        # self.recv_buff_size_computer.max_recv_buff_size = 3145728
        self.recv_buff_size_computer.max_recv_buff_size = 10 * 1024**2
        # self.recv_buff_size_computer.max_recv_buff_size = 1024
        print(f'max_recv_buff_size: {self.recv_buff_size_computer.max_recv_buff_size}')
        self.limit_by_limit: bool = True
        self.limit_by_global_in__data_size_limit: bool = True
    
    async def read_max(self):
        return await self.read(self._limit)
    
    async def read_nearly_max(self):
        return await self.read_nearly(self._limit)
    
    async def read_with_counter(self):
        if self._exception is not None:
            raise self._exception

        # This used to just loop creating a new waiter hoping to
        # collect everything in self._buffer, but that would
        # deadlock if the subprocess sends more than self.limit
        # bytes.  So just call self.read(self._limit) until EOF.
        blocks = []
        counter = 0
        while True:
            block = await self.read_max()
            counter += 1
            if not block:
                break
            blocks.append(block)
        return b''.join(blocks), counter

    def __repr__(self):
        info = ['TcpStreamReader']
        if self._smart_buffer.size():
            info.append(f'{self._smart_buffer.size()} bytes')
        if self._eof:
            info.append('eof')
        if self._limit != DEFAULT_LIMIT:
            info.append(f'limit={self._limit}')
        if self._waiter:
            info.append(f'waiter={self._waiter!r}')
        if self._exception:
            info.append(f'exception={self._exception!r}')
        if self._transport:
            info.append(f'transport={self._transport!r}')
        if self._paused:
            info.append('paused')
        return '<{}>'.format(' '.join(info))

    def _maybe_resume_transport(self):
        if isinstance(self._transport, (
            proactor_events._ProactorDatagramTransport,
            selector_events._SelectorTransport,
            unix_events._UnixReadPipeTransport
            )):
            # if hasattr(self._transport, 'max_size'):
            try:
                self._transport.max_size = self.recv_buff_size_computer.recv_buff_size
                # print(f'max_size: {self._transport.max_size}')
            except AttributeError:
                pass
        else:
            print(f'Unsupported transport: {type(self._transport)}')
        
        if self._paused \
            and (
                ((not self.limit_by_limit) and (not self.limit_by_global_in__data_size_limit)) \
                or (self.limit_by_limit and (not self._limit)) \
                or (self.limit_by_limit and (self._smart_buffer.size() <= self._limit)) \
                or (self.limit_by_global_in__data_size_limit and (not self._stream_manager.io_memory_management.global_in__data_size_limit)) \
                or (self.limit_by_global_in__data_size_limit and (self._stream_manager.io_memory_management.global_in__data_full_size.value <= self._stream_manager.io_memory_management.global_in__data_size_limit.value))
            ):
            self._paused = False
            self._transport.resume_reading()

    def at_eof(self):
        """Return True if the buffer is empty and 'feed_eof' was called."""
        return self._eof and not self._smart_buffer.size()

    def feed_data(self, data):
        assert not self._eof, 'feed_data after feed_eof'

        if not data:
            return

        data_len = len(data)
        self.recv_buff_size_computer.calc_new_recv_buff_size(data_len)
        self._smart_buffer.add_piece_of_data(data)
        self._wakeup_waiter()

        if (self._transport is not None and
                not self._paused 
                and (
                    (self.limit_by_limit and (self._smart_buffer.size() > 2 * self._limit)
                    or (self.limit_by_global_in__data_size_limit and (self._stream_manager.io_memory_management.global_in__data_full_size.value > self._stream_manager.io_memory_management.global_in__data_size_limit.value)))
                )):
            try:
                self._transport.pause_reading()
            except NotImplementedError:
                # The transport can't be paused.
                # We'll just have to buffer all data.
                # Forget the transport so we don't keep trying.
                self._transport = None
            else:
                self._paused = True

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
        sep = b'\n'
        seplen = len(sep)
        try:
            line = await self.readuntil(sep)
        except IncompleteReadError as e:
            return e.partial
        except LimitOverrunError as e:
            if self._smart_buffer.startswith(sep, e.consumed):
                self._smart_buffer.get_data(e.consumed + seplen)
            else:
                self._smart_buffer.clear()
            
            self._maybe_resume_transport()
            raise ValueError(e.args[0])
        return line

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
        seplen = len(separator)
        if seplen == 0:
            raise ValueError('Separator should be at least one-byte string')

        if self._exception is not None:
            raise self._exception

        # Consume whole buffer except last bytes, which length is
        # one less than seplen. Let's check corner cases with
        # separator='SEPARATOR':
        # * we have received almost complete separator (without last
        #   byte). i.e buffer='some textSEPARATO'. In this case we
        #   can safely consume len(separator) - 1 bytes.
        # * last byte of buffer is first byte of separator, i.e.
        #   buffer='abcdefghijklmnopqrS'. We may safely consume
        #   everything except that last byte, but this require to
        #   analyze bytes of buffer that match partial separator.
        #   This is slow and/or require FSM. For this case our
        #   implementation is not optimal, since require rescanning
        #   of data that is known to not belong to separator. In
        #   real world, separator will not be so long to notice
        #   performance problems. Even when reading MIME-encoded
        #   messages :)

        # `offset` is the number of bytes from the beginning of the buffer
        # where there is no occurrence of `separator`.
        offset = 0

        # Loop until we find `separator` in the buffer, exceed the buffer size,
        # or an EOF has happened.
        while True:
            buflen = self._smart_buffer.size()

            # Check if we now have enough data in the buffer for `separator` to
            # fit.
            if buflen - offset >= seplen:
                isep = self._smart_buffer.find(separator, offset)

                if isep != -1:
                    # `separator` is in the buffer. `isep` will be used later
                    # to retrieve the data.
                    break

                # see upper comment for explanation.
                offset = buflen + 1 - seplen
                if offset > self._limit:
                    raise LimitOverrunError(
                        'Separator is not found, and chunk exceed the limit',
                        offset)

            # Complete message (with full separator) may be present in buffer
            # even when EOF flag is set. This may happen when the last chunk
            # adds data which makes separator be found. That's why we check for
            # EOF *ater* inspecting the buffer.
            if self._eof:
                chunk = self._smart_buffer.get_data(self._smart_buffer.size())
                raise IncompleteReadError(chunk, None)

            # _wait_for_data() will resume reading if stream was paused.
            await self._wait_for_data('readuntil')

        if isep > self._limit:
            raise LimitOverrunError(
                'Separator is found, but chunk is longer than limit', isep)

        chunk = self._smart_buffer.get_data(isep + seplen)
        self._maybe_resume_transport()
        return bytes(chunk)

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

        if self._exception is not None:
            raise self._exception

        if n == 0:
            return b''

        if n < 0:
            # This used to just loop creating a new waiter hoping to
            # collect everything in self._buffer, but that would
            # deadlock if the subprocess sends more than self.limit
            # bytes.  So just call self.read(self._limit) until EOF.
            blocks = []
            while True:
                block = await self.read_nearly(max(self._limit, self._smart_buffer.size()))
                if not block:
                    break
                blocks.append(block)
            return b''.join(blocks)

        if not self._smart_buffer.size() and not self._eof:
            await self._wait_for_data('read')

        # This will work right even if buffer is less than n bytes
        data = self._smart_buffer.get_data(min(n, self._smart_buffer.size()))

        self._maybe_resume_transport()
        return data

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

        if self._exception is not None:
            raise self._exception

        if n == 0:
            return b''

        if n < 0:
            # This used to just loop creating a new waiter hoping to
            # collect everything in self._buffer, but that would
            # deadlock if the subprocess sends more than self.limit
            # bytes.  So just call self.read(self._limit) until EOF.
            blocks = []
            while True:
                block = await self.read_nearly(max(self._limit, self._smart_buffer.size()))
                if not block:
                    break
                blocks.append(block)
            return b''.join(blocks)

        if not self._smart_buffer.size() and not self._eof:
            await self._wait_for_data('read')

        # This will work right even if buffer is less than n bytes
        data = self._smart_buffer.get_data_nearly(n)

        self._maybe_resume_transport()
        return data

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
        if n < 0:
            raise ValueError('readexactly size can not be less than zero')

        if self._exception is not None:
            raise self._exception

        if n == 0:
            return b''

        while self._smart_buffer.size() < n:
            if self._eof:
                incomplete = self._smart_buffer.get_data(self._smart_buffer.size())
                raise IncompleteReadError(incomplete, n)

            await self._wait_for_data('readexactly')

        if self._smart_buffer.size() == n:
            data = self._smart_buffer.get_data(self._smart_buffer.size())
        else:
            data = self._smart_buffer.get_data(n)

        self._maybe_resume_transport()
        return data
    
    async def readonly_exactly(self, n):
        if n < 0:
            raise ValueError('readexactly size can not be less than zero')

        if self._exception is not None:
            raise self._exception

        if n == 0:
            return b''

        while self._smart_buffer.size() < n:
            if self._eof:
                incomplete = self._smart_buffer.read_data(self._smart_buffer.size())
                raise IncompleteReadError(incomplete, n)

            await self._wait_for_data('readexactly')

        if self._smart_buffer.size() == n:
            data = self._smart_buffer.read_data(self._smart_buffer.size())
        else:
            data = self._smart_buffer.read_data(n)

        self._maybe_resume_transport()
        return data
    
    async def read_message(self):
        message_len_encoded = await self.readexactly(self._message_protocol_settings._message_size_len)
        message_len = int.from_bytes(message_len_encoded, 'little')
        return await self.readexactly(message_len)
    
    def message_awailable(self) -> bool:
        message_size_len = self._message_protocol_settings._message_size_len
        if self._smart_buffer.size() < message_size_len:
            return False

        message_len_encoded = self._smart_buffer.get_data(message_size_len)
        message_len = int.from_bytes(message_len_encoded, 'little')
        if self._smart_buffer.size() < (message_size_len + message_len):
            return False
        
        return True
    
    def transport_pause_reading(self):
        try:
            self._transport.pause_reading()
        except NotImplementedError:
            # The transport can't be paused.
            # We'll just have to buffer all data.
            # Forget the transport so we don't keep trying.
            pass
        else:
            self._paused = True
    
    def transport_resume_reading(self):
        self._paused = False
        self._transport.resume_reading()


# class StreamReaderProtocolCopy(OriginalStreamReaderProtocol):
#     def __init__(self, manager: TcpStreamManager, original_stream_reader_protocol: OriginalStreamReaderProtocol) -> None:
#         self._stream_manager = manager
#         original_dict: dict = copy(original_stream_reader_protocol.__dict__)
#         original_dict.pop('_stream_manager', None)
#         original_dict.pop('_client_connected_cb', None)
#         self.__dict__.update(original_dict)
#         self._original__client_connected_cb = None
#         self._client_connected_cb = original_stream_reader_protocol._client_connected_cb
    
#     async def _wrapper__client_connected_cb(self, reader: OriginalStreamReader, writer: OriginalStreamWriter):
#         self._stream_writer = StreamWriterCopy(self._stream_manager, writer)
#         if self._original__client_connected_cb is not None:
#             await self._original__client_connected_cb(reader, self._stream_writer)
    
#     @property
#     def _client_connected_cb(self):
#         if self._original__client_connected_cb is None:
#             return None
#         else:
#             return self._wrapper__client_connected_cb
    
#     @_client_connected_cb.setter
#     def _client_connected_cb(self, value):
#         self._original__client_connected_cb = value


class TcpStreamReaderProtocol(OriginalStreamReaderProtocol, StreamReaderProtocolAbstract):
    def __init__(self, manager: TcpStreamManager, message_protocol_settings: MessageProtocolSettings, *args, **kwargs) -> None:
        self._bind_to_stream_manager(manager, message_protocol_settings, *args, **kwargs)

    def _bind_to_stream_manager(self, manager: TcpStreamManager, message_protocol_settings: MessageProtocolSettings, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._stream_manager = manager
        self._message_protocol_settings: MessageProtocolSettings = message_protocol_settings

    def connection_made(self, transport):
        if self._reject_connection:
            context = {
                'message': ('An open stream was garbage collected prior to '
                            'establishing network connection; '
                            'call "stream.close()" explicitly.')
            }
            if self._source_traceback:
                context['source_traceback'] = self._source_traceback
            self._loop.call_exception_handler(context)
            transport.abort()
            return
        
        self._transport = transport
        reader = self._stream_reader
        if reader is not None:
            reader.set_transport(transport)

        self._over_ssl = transport.get_extra_info('sslcontext') is not None
        if self._client_connected_cb is not None:
            self._stream_writer = TcpStreamWriter(transport, self,
                                               reader,
                                               self._loop)
            res = self._client_connected_cb(reader,
                                            self._stream_writer)
            if coroutines.iscoroutine(res):
                self._loop.create_task(res)
            
            self._strong_reader = None


# class StreamWriterCopy(OriginalStreamWriter):
#     def __init__(self, manager: TcpStreamManager, original_stream_writer: OriginalStreamWriter) -> None:
#         self._stream_manager = manager
#         self._output_to_client: DynamicListOfPiecesDequeWithLengthControl = self._stream_manager.output_to_client_container_type(
#             external_data_length=self._stream_manager.io_memory_management.global_out__data_full_size)
#         self.socket_write_fixed_buffer_size: ValueExistence = self._stream_manager.io_memory_management.socket_write_fixed_buffer_size
#         self._autonomous_writer_future: Task = None
#         self._autonomous_writer_future_stop_requessted: bool = False
#         self._autonomous_writer_drain_enough_futures: List[Future] = list()
#         original_dict: dict = copy(original_stream_writer.__dict__)
#         original_dict.pop('_stream_manager', None)
#         original_dict.pop('_output_to_client', None)
#         original_dict.pop('_autonomous_writer_future_stop_requessted', None)
#         self.__dict__.update(original_dict)
    
#     def optimized_write(self, data):
#         # self._output_to_client.add_piece_of_data(data)
#         self.write(data)

#     def owrite(self, data):
#         return self.optimized_write(data)

#     async def partial_drain(self):
#         await self.drain()
#         # another_piece_of_data = self._output_to_client.get_data(self.socket_write_fixed_buffer_size.value)
#         # while another_piece_of_data:
#         #     self.write(another_piece_of_data)
#         #     await self.drain()
#         #     another_piece_of_data = self._output_to_client.get_data(self.socket_write_fixed_buffer_size.value)

#     async def pdrain(self):
#         return await self.partial_drain()

#     async def full_drain(self):
#         await self.pdrain()
#         rest_of_the_data_size = self._output_to_client.size()
#         if rest_of_the_data_size:
#             another_piece_of_data = self._output_to_client.get_data(rest_of_the_data_size)
#             self.write(another_piece_of_data)
#             await self.drain()

#     async def fdrain(self):
#         return await self.full_drain()
    
#     def _release_autonomous_writer_waiters(self):
#         current_size = self._output_to_client.size()
#         autonomous_writer_drain_enough_futures_buff = self._autonomous_writer_drain_enough_futures
#         self._autonomous_writer_drain_enough_futures = type(autonomous_writer_drain_enough_futures_buff)()
#         for item in autonomous_writer_drain_enough_futures_buff:
#             lower_water_size, future = item
#             if current_size < lower_water_size:
#                 if (not future.done()) and (not future.cancelled()):
#                     future.set_result(None)

#             if (not future.done()) and (not future.cancelled()):
#                 self._autonomous_writer_drain_enough_futures.append(item)
    
#     async def _autonomous_writer_impl(self):
#         ty = TimedYield(0)
#         while not self._autonomous_writer_future_stop_requessted:
#             another_piece_of_data = self._output_to_client.get_data(self.socket_write_fixed_buffer_size.value)
#             self._release_autonomous_writer_waiters()
#             while another_piece_of_data:
#                 self.write(another_piece_of_data)
#                 await self.drain()
#                 another_piece_of_data = self._output_to_client.get_data(self.socket_write_fixed_buffer_size.value)
#                 self._release_autonomous_writer_waiters()
            
#             await ty()
    
#     def start_autonomous_writer(self):
#         self._autonomous_writer_future = create_task(self._autonomous_writer_impl)
    
#     def start_aw(self):
#         return self.start_autonomous_writer()
    
#     async def stop_autonomous_writer(self, timeout: Optional[Union[int, float]] = 0):
#         """_summary_

#         Args:
#             timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout

#         Returns:
#             _type_: _description_
#         """
#         result = None
#         if timeout is None:
#             timeout = self._stream_manager.autonomous_writer_stop_default_timeout
        
#         if self._autonomous_writer_future and (not self._autonomous_writer_future_stop_requessted):
#             self._autonomous_writer_future_stop_requessted = True
#             if timeout:
#                 result = await asyncio.wait_for(self._autonomous_writer_future, timeout)
#             else:
#                 result = await self._autonomous_writer_future
            
#             self._autonomous_writer_future = None
#             self._autonomous_writer_future_stop_requessted = False
        
#         return result
    
#     def stop_ar(self, timeout: Optional[Union[int, float]] = 0):
#         """_summary_

#         Args:
#             timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout

#         Returns:
#             _type_: _description_
#         """
#         return self.stop_autonomous_writer(timeout)
    
#     async def autonomous_writer_drain_enough(self, lower_water_size: Optional[int] = None):
#         if lower_water_size is None:
#             lower_water_size = self.socket_write_fixed_buffer_size.value * 2
        
#         if lower_water_size <= self._output_to_client.size():
#             future: Future = self._loop.create_future()
#             self._autonomous_writer_drain_enough_futures.append((lower_water_size, future))
#             await future

    
#     async def ar_drain_enough(self):
#         await self.autonomous_writer_drain_enough()


class TcpStreamWriter(OriginalStreamWriter, StreamWriterAbstract):
    def __init__(self, *args, **kwargs) -> None:
        self._bind_to_stream_manager(*args, **kwargs)

    def _bind_to_stream_manager(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._stream_manager: TcpStreamManager = self._protocol._stream_manager
        self._output_to_client: DynamicListOfPiecesDequeWithLengthControl = self._stream_manager.output_to_client_container_type(
            external_data_length=self._stream_manager.io_memory_management.global_out__data_full_size)
        self.socket_write_fixed_buffer_size: ValueExistence = self._stream_manager.io_memory_management.socket_write_fixed_buffer_size
        self._autonomous_writer_future: Task = None
        self._autonomous_writer_future_stop_requessted: bool = False
        self._autonomous_writer_drain_enough_futures: List[Future] = list()

    def optimized_write(self, data):
        self._output_to_client.add_piece_of_data(data)
        # self.write(data)

    def owrite(self, data):
        return self.optimized_write(data)

    async def partial_drain(self):
        another_piece_of_data = self._output_to_client.get_data(self.socket_write_fixed_buffer_size.value)
        while another_piece_of_data:
            self.write(another_piece_of_data)
            await self.drain()
            another_piece_of_data = self._output_to_client.get_data(self.socket_write_fixed_buffer_size.value)

    async def pdrain(self):
        return await self.partial_drain()

    async def full_drain(self):
        await self.pdrain()
        rest_of_the_data_size = self._output_to_client.size()
        if rest_of_the_data_size:
            another_piece_of_data = self._output_to_client.get_data(rest_of_the_data_size)
            self.write(another_piece_of_data)
            await self.drain()

    async def fdrain(self):
        return await self.full_drain()
    
    def _release_autonomous_writer_waiters(self):
        current_size = self._output_to_client.size()
        autonomous_writer_drain_enough_futures_buff = self._autonomous_writer_drain_enough_futures
        self._autonomous_writer_drain_enough_futures = type(autonomous_writer_drain_enough_futures_buff)()
        for item in autonomous_writer_drain_enough_futures_buff:
            lower_water_size, future = item
            if current_size < lower_water_size:
                if (not future.done()) and (not future.cancelled()):
                    future.set_result(None)

            if (not future.done()) and (not future.cancelled()):
                self._autonomous_writer_drain_enough_futures.append(item)
    
    async def _autonomous_writer_impl(self):
        ty = TimedYield(0)
        while not self._autonomous_writer_future_stop_requessted:
            another_piece_of_data = self._output_to_client.get_data(self.socket_write_fixed_buffer_size.value)
            self._release_autonomous_writer_waiters()
            while another_piece_of_data:
                self.write(another_piece_of_data)
                await self.drain()
                another_piece_of_data = self._output_to_client.get_data(self.socket_write_fixed_buffer_size.value)
                self._release_autonomous_writer_waiters()
            
            await ty()
    
    def start_autonomous_writer(self):
        self._autonomous_writer_future = create_task(self._autonomous_writer_impl)
    
    def start_aw(self):
        return self.start_autonomous_writer()
    
    async def stop_autonomous_writer(self, timeout: Optional[Union[int, float]] = 0):
        """_summary_

        Args:
            timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout

        Returns:
            _type_: _description_
        """
        result = None
        if timeout is None:
            timeout = self._stream_manager.autonomous_writer_stop_default_timeout
        
        if self._autonomous_writer_future and (not self._autonomous_writer_future_stop_requessted):
            self._autonomous_writer_future_stop_requessted = True
            if timeout:
                result = await asyncio.wait_for(self._autonomous_writer_future, timeout)
            else:
                result = await self._autonomous_writer_future
            
            self._autonomous_writer_future = None
            self._autonomous_writer_future_stop_requessted = False
        
        return result
    
    def stop_ar(self, timeout: Optional[Union[int, float]] = 0):
        """_summary_

        Args:
            timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout

        Returns:
            _type_: _description_
        """
        return self.stop_autonomous_writer(timeout)
    
    async def autonomous_writer_drain_enough(self, lower_water_size: Optional[int] = None):
        if lower_water_size is None:
            lower_water_size = self.socket_write_fixed_buffer_size.value * 3
            # print(f'lower_water_size: {lower_water_size}')
            # lower_water_size = CpuInfo().l3_cache_size
        
        if lower_water_size <= self._output_to_client.size():
            future: Future = self._loop.create_future()
            self._autonomous_writer_drain_enough_futures.append((lower_water_size, future))
            await future
    
    async def ar_drain_enough(self):
        await self.autonomous_writer_drain_enough()
    
    def optimized_write_message(self, data):
        self.optimized_write(len(data).to_bytes(self._protocol._message_protocol_settings._message_size_len, 'little') + data)
    
    def owrite_message(self, data):
        self.optimized_write_message(data)
    
    async def send_message(self, data):
        self.optimized_write_message(data)
        await self.fdrain()
