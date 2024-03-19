# open_connection

```python
async def open_connection(host=None, port=None, *,
                          loop=None, limit=_DEFAULT_LIMIT, **kwds) -> Tuple[StreamReader, StreamWriter]:
    """A wrapper for create_connection() returning a (reader, writer) pair.

    The reader returned is a StreamReader instance; the writer is a
    StreamWriter instance.

    The arguments are all the usual arguments to create_connection()
    except protocol_factory; most common are positional host and port,
    with various optional keyword arguments following.

    Additional optional keyword arguments are loop (to set the event loop
    instance to use) and limit (to set the buffer limit passed to the
    StreamReader).

    (If you want to customize the StreamReader and/or
    StreamReaderProtocol classes, just copy the code -- there's
    really nothing special here except some convenience.)
    """
```

## FULL: StreamReader

```python
class StreamReader:

    _source_traceback = None

    def __init__(self, limit=_DEFAULT_LIMIT, loop=None):
        # The line length limit is  a security feature;
        # it also doubles as half the buffer limit.
        raise NotImplementedError
```
