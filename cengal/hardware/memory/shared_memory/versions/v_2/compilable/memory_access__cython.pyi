__all__ = ['write_uint64', 'read_uint64', 'zero_memory']


from typing import Callable, Any


def write_uint64(base_address: int, offset: int, value: int) -> None: ...
def write_int64(base_address: int, offset: int, value: int) -> None: ...
def write_uint32(base_address: int, offset: int, value: int) -> None: ...
def write_int32(base_address: int, offset: int, value: int) -> None: ...
def write_uint16(base_address: int, offset: int, value: int) -> None: ...
def write_int16(base_address: int, offset: int, value: int) -> None: ...
def write_uint8(base_address: int, offset: int, value: int) -> None: ...
def write_int8(base_address: int, offset: int, value: int) -> None: ...
def write_float(base_address: int, offset: int, value: int) -> None: ...
def write_double(base_address: int, offset: int, value: int) -> None: ...


def read_uint64(base_address: int, offset: int) -> int: ...
def read_int64(base_address: int, offset: int) -> int: ...
def read_uint32(base_address: int, offset: int) -> int: ...
def read_int32(base_address: int, offset: int) -> int: ...
def read_uint16(base_address: int, offset: int) -> int: ...
def read_int16(base_address: int, offset: int) -> int: ...
def read_uint8(base_address: int, offset: int) -> int: ...
def read_int8(base_address: int, offset: int) -> int: ...
def read_float(base_address: int, offset: int) -> int: ...
def read_double(base_address: int, offset: int) -> int: ...


def zero_memory(base_address: int, offset: int, size: int) -> None: ...


def mask_least_significant_bits(hash_value: int, n: int) -> int: ...


def list__get_item(key: int, base_address: int, offset__pointer_to_internal_list: int, get_obj_callback: Callable) -> int: ...
def list__set_item(key: int, value: Any, base_address: int, offset__pointer_to_internal_list: int, put_obj_callback: Callable) -> int: ...
