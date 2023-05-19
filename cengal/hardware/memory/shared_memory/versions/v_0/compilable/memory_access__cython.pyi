__all__ = ['write_uint64', 'read_uint64', 'zero_memory']


def write_uint64(base_address: int, offset: int, value: int) -> None: ...
def read_uint64(base_address: int, offset: int) -> int: ...
def zero_memory(base_address: int, offset: int, size: int) -> None: ...