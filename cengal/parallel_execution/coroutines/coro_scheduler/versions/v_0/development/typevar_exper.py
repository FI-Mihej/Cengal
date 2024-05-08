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
__version__ = "4.4.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from typing import Generic, overload, Type, TypeVar, Union, Optional, Tuple, Text, Dict



T = TypeVar('T')


def interface_method(method):
    def wrapper(*args, **kwargs):
        method(*args, **kwargs)
        print(method.__self__)


class Request:
    def __init__(self) -> None:
        ...
    
    def __call__(self, x: int, y: Text, b: float) -> 'Request':
        ...

    # @interface_method
    def i(self) -> Tuple[int, Dict[str, float]]:
        ...


class SingleRequest(Request):
    def __call__(self, x: int, xx: Text, bb: float, vv: Tuple) -> 'SingleRequest':
        ...

    # @interface_method
    def i(self) -> Tuple[Text, Dict[int, float]]:
        super().i()
        ...


def interface(request_type: Type[T]) -> T:
    return request_type()


i = interface


i(Request)(1, 's', 1.0).i()
Request()(1, 's', 1.0).i()
i(SingleRequest)(1, 's', 1.0, tuple()).i()
SingleRequest()(1, 's', 1.0, tuple()).i()
