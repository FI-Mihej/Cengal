# create_datagram_endpoint

```python
async def create_datagram_endpoint() -> Tuple[Union[_SelectorDatagramTransport, _ProactorDatagramTransport], DatagramProtocol]
```

## PARTS OF: DatagramProtocol

### DatagramProtocol

```python
class DatagramProtocol(BaseProtocol):
    """Interface for datagram protocol."""

    __slots__ = ()

    def datagram_received(self, data, addr):
        """Called when some datagram is received."""

    def error_received(self, exc):
        """Called when a send or receive operation raises an OSError.

        (Other than BlockingIOError or InterruptedError.)
        """
```

### BaseProtocol

```python
class BaseProtocol:
    """Common base class for protocol interfaces.

    Usually user implements protocols that derived from BaseProtocol
    like Protocol or ProcessProtocol.

    The only case when BaseProtocol should be implemented directly is
    write-only transport like write pipe
    """

    __slots__ = ()

    def connection_made(self, transport):
        """Called when a connection is made.

        The argument is the transport representing the pipe connection.
        To receive data, wait for data_received() calls.
        When the connection is closed, connection_lost() is called.
        """

    def connection_lost(self, exc):
        """Called when the connection is lost or closed.

        The argument is an exception object or None (the latter
        meaning a regular EOF is received or the connection was
        aborted or closed).
        """

    def pause_writing(self):
        """Called when the transport's buffer goes over the high-water mark.

        Pause and resume calls are paired -- pause_writing() is called
        once when the buffer goes strictly over the high-water mark
        (even if subsequent writes increases the buffer size even
        more), and eventually resume_writing() is called once when the
        buffer size reaches the low-water mark.

        Note that if the buffer size equals the high-water mark,
        pause_writing() is not called -- it must go strictly over.
        Conversely, resume_writing() is called when the buffer size is
        equal or lower than the low-water mark.  These end conditions
        are important to ensure that things go as expected when either
        mark is zero.

        NOTE: This is the only Protocol callback that is not called
        through EventLoop.call_soon() -- if it were, it would have no
        effect when it's most needed (when the app keeps writing
        without yielding until pause_writing() is called).
        """

    def resume_writing(self):
        """Called when the transport's buffer drains below the low-water mark.

        See pause_writing() for details.
        """
```

## FULL: DatagramProtocol

```python
class DatagramProtocol(BaseProtocol):
    """Interface for datagram protocol."""
    """Common base class for protocol interfaces.

    Usually user implements protocols that derived from BaseProtocol
    like Protocol or ProcessProtocol.

    The only case when BaseProtocol should be implemented directly is
    write-only transport like write pipe
    """

    __slots__ = ()

    def datagram_received(self, data, addr):
        """Called when some datagram is received."""

    def error_received(self, exc):
        """Called when a send or receive operation raises an OSError.

        (Other than BlockingIOError or InterruptedError.)
        """

    def connection_made(self, transport):
        """Called when a connection is made.

        The argument is the transport representing the pipe connection.
        To receive data, wait for data_received() calls.
        When the connection is closed, connection_lost() is called.
        """

    def connection_lost(self, exc):
        """Called when the connection is lost or closed.

        The argument is an exception object or None (the latter
        meaning a regular EOF is received or the connection was
        aborted or closed).
        """

    def pause_writing(self):
        """Called when the transport's buffer goes over the high-water mark.

        Pause and resume calls are paired -- pause_writing() is called
        once when the buffer goes strictly over the high-water mark
        (even if subsequent writes increases the buffer size even
        more), and eventually resume_writing() is called once when the
        buffer size reaches the low-water mark.

        Note that if the buffer size equals the high-water mark,
        pause_writing() is not called -- it must go strictly over.
        Conversely, resume_writing() is called when the buffer size is
        equal or lower than the low-water mark.  These end conditions
        are important to ensure that things go as expected when either
        mark is zero.

        NOTE: This is the only Protocol callback that is not called
        through EventLoop.call_soon() -- if it were, it would have no
        effect when it's most needed (when the app keeps writing
        without yielding until pause_writing() is called).
        """

    def resume_writing(self):
        """Called when the transport's buffer drains below the low-water mark.

        See pause_writing() for details.
        """
```

## PARTS OF: _SelectorDatagramTransport

### _SelectorDatagramTransport

```python
class _SelectorDatagramTransport(_SelectorTransport):
    def __init__(self, loop, sock, protocol, address=None,
                 waiter=None, extra=None):
        raise NotImplementedError

    def get_write_buffer_size(self) -> int:
        raise NotImplementedError

    def _read_ready(self) -> None:
        raise NotImplementedError

    def sendto(self, data, addr=None) -> None:
        raise NotImplementedError

    def _sendto_ready(self) -> None:
        raise NotImplementedError
```

### _SelectorTransport

```python
class _SelectorTransport(transports._FlowControlMixin,
                         transports.Transport):

    max_size = 256 * 1024  # Buffer size passed to recv().

    _buffer_factory = bytearray  # Constructs initial value for self._buffer.

    # Attribute used in the destructor: it must be set even if the constructor
    # is not called (see _SelectorSslTransport which may start by raising an
    # exception)
    _sock = None

    def __init__(self, loop, sock, protocol, extra=None, server=None):
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def abort(self) -> None:
        raise NotImplementedError

    def set_protocol(self, protocol: DatagramProtocol) -> None:
        raise NotImplementedError

    def is_closing(self) -> bool:
        raise NotImplementedError

    def __del__(self, _warn=warnings.warn) -> None:
        raise NotImplementedError

    def _fatal_error(self, exc, message='Fatal error on transport') -> None:
        # Should be called from exception handler only.
        raise NotImplementedError

    def _force_close(self, exc) -> None:
        raise NotImplementedError

    def _call_connection_lost(self, exc) -> None:
        raise NotImplementedError

    def get_write_buffer_size(self) -> int:
        raise NotImplementedError

    def _add_reader(self, fd, callback, *args) -> None:
        raise NotImplementedError
```

### _FlowControlMixin

```python
class _FlowControlMixin(Transport):
    def __init__(self, extra=None, loop=None):
        raise NotImplementedError

    def _maybe_pause_protocol(self) -> None:
        raise NotImplementedError

    def _maybe_resume_protocol(self) -> None:
        raise NotImplementedError

    def get_write_buffer_limits(self) -> Tuple[int, int]:
        raise NotImplementedError

    def _set_write_buffer_limits(self, high=None, low=None) -> None:
        raise NotImplementedError

    def set_write_buffer_limits(self, high=None, low=None) -> None:
        raise NotImplementedError

    def get_write_buffer_size(self) -> int:
        raise NotImplementedError
```

### Transport

```python
class Transport(ReadTransport, WriteTransport):
    pass
```

### ReadTransport

```python
class ReadTransport(BaseTransport):

    def is_reading(self) -> bool:
        """Return True if the transport is receiving."""
        raise NotImplementedError

    def pause_reading(self) -> None:
        """Pause the receiving end.

        No data will be passed to the protocol's data_received()
        method until resume_reading() is called.
        """
        raise NotImplementedError

    def resume_reading(self) -> None:
        """Resume the receiving end.

        Data received will once again be passed to the protocol's
        data_received() method.
        """
        raise NotImplementedError
```

### WriteTransport

```python
class WriteTransport(BaseTransport):

    def set_write_buffer_limits(self, high=None, low=None):
        """Set the high- and low-water limits for write flow control.

        These two values control when to call the protocol's
        pause_writing() and resume_writing() methods.  If specified,
        the low-water limit must be less than or equal to the
        high-water limit.  Neither value can be negative.

        The defaults are implementation-specific.  If only the
        high-water limit is given, the low-water limit defaults to an
        implementation-specific value less than or equal to the
        high-water limit.  Setting high to zero forces low to zero as
        well, and causes pause_writing() to be called whenever the
        buffer becomes non-empty.  Setting low to zero causes
        resume_writing() to be called only once the buffer is empty.
        Use of zero for either limit is generally sub-optimal as it
        reduces opportunities for doing I/O and computation
        concurrently.
        """
        raise NotImplementedError

    def get_write_buffer_size(self):
        """Return the current size of the write buffer."""
        raise NotImplementedError

    def write(self, data):
        """Write some data bytes to the transport.

        This does not block; it buffers the data and arranges for it
        to be sent out asynchronously.
        """
        raise NotImplementedError

    def writelines(self, list_of_data):
        """Write a list (or any iterable) of data bytes to the transport.

        The default implementation concatenates the arguments and
        calls write() on the result.
        """
        data = b''.join(list_of_data)
        self.write(data)

    def write_eof(self):
        """Close the write end after flushing buffered data.

        (This is like typing ^D into a UNIX program reading from stdin.)

        Data may still be received.
        """
        raise NotImplementedError

    def can_write_eof(self):
        """Return True if this transport supports write_eof(), False if not."""
        raise NotImplementedError

    def abort(self):
        """Close the transport immediately.

        Buffered data will be lost.  No more data will be received.
        The protocol's connection_lost() method will (eventually) be
        called with None as its argument.
        """
        raise NotImplementedError
```

### BaseTransport

```python
class BaseTransport:
    def __init__(self, extra=None):
        raise NotImplementedError

    def get_extra_info(self, name, default=None):
        """Get optional transport information."""
        return self._extra.get(name, default)

    def is_closing(self):
        """Return True if the transport is closing or closed."""
        raise NotImplementedError

    def close(self):
        """Close the transport.

        Buffered data will be flushed asynchronously.  No more data
        will be received.  After all buffered data is flushed, the
        protocol's connection_lost() method will (eventually) be
        called with None as its argument.
        """
        raise NotImplementedError

    def set_protocol(self, protocol: DatagramProtocol):
        """Set a new protocol."""
        raise NotImplementedError

    def get_protocol(self) -> DatagramProtocol:
        """Return the current protocol."""
        raise NotImplementedError
```

## FULL: _SelectorDatagramTransport

```python
class _SelectorDatagramTransport(_SelectorTransport):
    max_size = 256 * 1024  # Buffer size passed to recv().

    _buffer_factory = bytearray  # Constructs initial value for self._buffer.

    # Attribute used in the destructor: it must be set even if the constructor
    # is not called (see _SelectorSslTransport which may start by raising an
    # exception)
    _sock = None

    def __init__(self, loop, sock, protocol, address=None,
                 waiter=None, extra=None):
        raise NotImplementedError

    def _read_ready(self) -> None:
        raise NotImplementedError

    def sendto(self, data, addr=None) -> None:
        raise NotImplementedError

    def _sendto_ready(self) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def abort(self) -> None:
        raise NotImplementedError

    def __del__(self, _warn=warnings.warn) -> None:
        raise NotImplementedError

    def _fatal_error(self, exc, message='Fatal error on transport') -> None:
        # Should be called from exception handler only.
        raise NotImplementedError

    def _force_close(self, exc) -> None:
        raise NotImplementedError

    def _call_connection_lost(self, exc) -> None:
        raise NotImplementedError

    def _add_reader(self, fd, callback, *args) -> None:
        raise NotImplementedError

    def _maybe_pause_protocol(self) -> None:
        raise NotImplementedError

    def _maybe_resume_protocol(self) -> None:
        raise NotImplementedError

    def get_write_buffer_limits(self) -> Tuple[int, int]:
        raise NotImplementedError

    def _set_write_buffer_limits(self, high=None, low=None) -> None:
        raise NotImplementedError

    def set_write_buffer_limits(self, high=None, low=None) -> None:
        raise NotImplementedError

    def get_write_buffer_size(self) -> int:
        raise NotImplementedError

    def is_reading(self) -> bool:
        """Return True if the transport is receiving."""
        raise NotImplementedError

    def pause_reading(self) -> None:
        """Pause the receiving end.

        No data will be passed to the protocol's data_received()
        method until resume_reading() is called.
        """
        raise NotImplementedError

    def resume_reading(self) -> None:
        """Resume the receiving end.

        Data received will once again be passed to the protocol's
        data_received() method.
        """
        raise NotImplementedError

    def get_extra_info(self, name, default=None):
        """Get optional transport information."""
        return self._extra.get(name, default)

    def is_closing(self):
        """Return True if the transport is closing or closed."""
        raise NotImplementedError

    def close(self):
        """Close the transport.

        Buffered data will be flushed asynchronously.  No more data
        will be received.  After all buffered data is flushed, the
        protocol's connection_lost() method will (eventually) be
        called with None as its argument.
        """
        raise NotImplementedError

    def set_protocol(self, protocol: DatagramProtocol):
        """Set a new protocol."""
        raise NotImplementedError

    def get_protocol(self) -> DatagramProtocol:
        """Return the current protocol."""
        raise NotImplementedError
```

## PARTS OF: _ProactorDatagramTransport

### _ProactorDatagramTransport

```python
class _ProactorDatagramTransport(_ProactorBasePipeTransport):
    max_size = 256 * 1024

    def __init__(self, loop, sock, protocol, address=None,
                 waiter=None, extra=None):
        raise NotImplementedError

    def _set_extra(self, sock) -> None:
        raise NotImplementedError

    def get_write_buffer_size(self) -> int:
        raise NotImplementedError

    def abort(self) -> None:
        raise NotImplementedError

    def sendto(self, data, addr=None) -> None:
        raise NotImplementedError

    def _loop_writing(self, fut=None) -> None:
        raise NotImplementedError

    def _loop_reading(self, fut=None) -> None:
        raise NotImplementedError

    def _sendto_ready(self) -> None:
        raise NotImplementedError

    def _sendto_ready(self) -> None:
        raise NotImplementedError
```

### _ProactorBasePipeTransport

```python
class _ProactorBasePipeTransport(transports._FlowControlMixin,
                                 transports.BaseTransport):

    def __init__(self, loop, sock, protocol, waiter=None,
                 extra=None, server=None):
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def _set_extra(self, sock) -> None:
        raise NotImplementedError

    def set_protocol(self, protocol: DatagramProtocol) -> None:
        raise NotImplementedError

    def get_protocol(self) -> DatagramProtocol:
        raise NotImplementedError

    def is_closing(self) -> bool:
        raise NotImplementedError

    def close(self) -> None:
        raise NotImplementedError

    def __del__(self, _warn=warnings.warn) -> None:
        raise NotImplementedError

    def _fatal_error(self, exc, message='Fatal error on pipe transport') -> None:
        raise NotImplementedError

    def _force_close(self, exc) -> None:
        raise NotImplementedError

    def _call_connection_lost(self, exc) -> None:
        raise NotImplementedError

    def get_write_buffer_size(self) -> int:
        raise NotImplementedError
```

## FULL: _ProactorDatagramTransport

```python
class _ProactorDatagramTransport(_ProactorBasePipeTransport):
    max_size = 256 * 1024

    def __init__(self, loop, sock, protocol, address=None,
                 waiter=None, extra=None):
        raise NotImplementedError

    def sendto(self, data, addr=None) -> None:
        raise NotImplementedError

    def _loop_writing(self, fut=None) -> None:
        raise NotImplementedError

    def _loop_reading(self, fut=None) -> None:
        raise NotImplementedError

    def _sendto_ready(self) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def _set_extra(self, sock) -> None:
        raise NotImplementedError

    def __del__(self, _warn=warnings.warn) -> None:
        raise NotImplementedError

    def _fatal_error(self, exc, message='Fatal error on pipe transport') -> None:
        raise NotImplementedError

    def _force_close(self, exc) -> None:
        raise NotImplementedError

    def _call_connection_lost(self, exc) -> None:
        raise NotImplementedError

    def _maybe_pause_protocol(self) -> None:
        raise NotImplementedError

    def _maybe_resume_protocol(self) -> None:
        raise NotImplementedError

    def get_write_buffer_limits(self) -> Tuple[int, int]:
        raise NotImplementedError

    def _set_write_buffer_limits(self, high=None, low=None) -> None:
        raise NotImplementedError
    
    def is_reading(self) -> bool:
        """Return True if the transport is receiving."""
        raise NotImplementedError

    def pause_reading(self) -> None:
        """Pause the receiving end.

        No data will be passed to the protocol's data_received()
        method until resume_reading() is called.
        """
        raise NotImplementedError

    def resume_reading(self) -> None:
        """Resume the receiving end.

        Data received will once again be passed to the protocol's
        data_received() method.
        """
        raise NotImplementedError

    def set_write_buffer_limits(self, high=None, low=None):
        """Set the high- and low-water limits for write flow control.

        These two values control when to call the protocol's
        pause_writing() and resume_writing() methods.  If specified,
        the low-water limit must be less than or equal to the
        high-water limit.  Neither value can be negative.

        The defaults are implementation-specific.  If only the
        high-water limit is given, the low-water limit defaults to an
        implementation-specific value less than or equal to the
        high-water limit.  Setting high to zero forces low to zero as
        well, and causes pause_writing() to be called whenever the
        buffer becomes non-empty.  Setting low to zero causes
        resume_writing() to be called only once the buffer is empty.
        Use of zero for either limit is generally sub-optimal as it
        reduces opportunities for doing I/O and computation
        concurrently.
        """
        raise NotImplementedError

    def get_write_buffer_size(self) -> int:
        """Return the current size of the write buffer."""
        raise NotImplementedError

    def write(self, data):
        """Write some data bytes to the transport.

        This does not block; it buffers the data and arranges for it
        to be sent out asynchronously.
        """
        raise NotImplementedError

    def writelines(self, list_of_data):
        """Write a list (or any iterable) of data bytes to the transport.

        The default implementation concatenates the arguments and
        calls write() on the result.
        """
        data = b''.join(list_of_data)
        self.write(data)

    def write_eof(self):
        """Close the write end after flushing buffered data.

        (This is like typing ^D into a UNIX program reading from stdin.)

        Data may still be received.
        """
        raise NotImplementedError

    def can_write_eof(self):
        """Return True if this transport supports write_eof(), False if not."""
        raise NotImplementedError

    def abort(self):
        """Close the transport immediately.

        Buffered data will be lost.  No more data will be received.
        The protocol's connection_lost() method will (eventually) be
        called with None as its argument.
        """
        raise NotImplementedError

    def get_extra_info(self, name, default=None):
        """Get optional transport information."""
        return self._extra.get(name, default)

    def is_closing(self):
        """Return True if the transport is closing or closed."""
        raise NotImplementedError

    def close(self):
        """Close the transport.

        Buffered data will be flushed asynchronously.  No more data
        will be received.  After all buffered data is flushed, the
        protocol's connection_lost() method will (eventually) be
        called with None as its argument.
        """
        raise NotImplementedError

    def set_protocol(self, protocol: DatagramProtocol):
        """Set a new protocol."""
        raise NotImplementedError

    def get_protocol(self) -> DatagramProtocol:
        """Return the current protocol."""
        raise NotImplementedError
```
