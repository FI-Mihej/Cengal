from typing import Dict, List, Any


NimObj = Dict[str, Any]


def serve(addr_list: List[NimObj]) -> List[NimObj]:
    ...


def client() -> NimObj:
    ...


def connect(addr_list: List[NimObj]) -> List[NimObj]:
    ...


def server_disconnect(reactorId: int, connectionId: int) -> bool:
    ...


def client_disconnect(reactorId: int, connectionId: int) -> bool:
    ...


def punch_through(address: NimObj):
    ...


def tick(server_send: Dict[int, List[NimObj]], client_send: Dict[int, List[NimObj]]) -> NimObj:
    ...
