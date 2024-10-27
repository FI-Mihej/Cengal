from enum import IntEnum

from typing import Optional, List, Dict, Type, Mapping


class Items(IntEnum):
    one = 1
    two = 2
    three = 3


items_num = len(Items)
items_names = [item.name for item in Items]
print(items_num)
print(items_names)

item_per_name = {item.name: item for item in Items}
print(item_per_name)
