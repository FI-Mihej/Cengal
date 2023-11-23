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


__all__ = ['cvalue_to_dict']


from ctypes import Structure, _Pointer, Array, c_char, c_wchar
from typing import Dict


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


def cvalue_to_dict(item) -> Dict:
    """_summary_
        Example:
            from pprintpp import pprint
            
            def wnd_proc_impl(self, hwnd: wintypes.HWND, msg: wintypes.UINT, wparam: wintypes.WPARAM, lparam: wintypes.LPARAM) -> LRESULT:
                if win32con.WM_NCCALCSIZE == msg:
                    lpnccalcsize_params = ctypes.cast(lparam, LPNCCALCSIZE_PARAMS)
                    print(f'WM_NCCALCSIZE: lpnccalcsize_params=')
                    pprint(ctypes_to_dict(lpnccalcsize_params))
                    print()
        
        Output:
            WM_NCCALCSIZE: lpnccalcsize_params=
            {
                'LP_NCCALCSIZE_PARAMS': {
                    'contents': {
                        'NCCALCSIZE_PARAMS': {
                            'lppos': {
                                'LP_WINDOWPOS': {
                                    'contents': {
                                        'WINDOWPOS': {
                                            'cx': 416,
                                            'cy': 240,
                                            'flags': 6199,
                                            'hwnd': 22679738,
                                            'hwndInsertAfter': None,
                                            'x': 507,
                                            'y': 114,
                                        },
                                    },
                                },
                            },
                            'rgrc': {
                                'RECT_Array_3': [
                                    {
                                        'RECT': {
                                            'bottom': 354,
                                            'left': 507,
                                            'right': 923,
                                            'top': 114,
                                        },
                                    },
                                    {
                                        'RECT': {
                                            'bottom': 354,
                                            'left': 507,
                                            'right': 923,
                                            'top': 114,
                                        },
                                    },
                                    {
                                        'RECT': {
                                            'bottom': 354,
                                            'left': 507,
                                            'right': 923,
                                            'top': 114,
                                        },
                                    },
                                ],
                            },
                        },
                    },
                },
            }
    
    Args:
        item (_type_): _description_

    Returns:
        Dict: _description_
    """    
    item_type_name = type(item).__name__
    if isinstance(item, Structure):
        st = item
        data = dict()
        fields = st._fields_
        for field_name, field_type in fields:
            field_value = cvalue_to_dict(getattr(st, field_name))
            data[field_name] = field_value
        
        return {item_type_name: data}
    elif isinstance(item, _Pointer):
        field_name = 'contents'
        field_value = cvalue_to_dict(item.contents)
        return {item_type_name: {field_name: field_value}}
    elif isinstance(item, Array):
        array_type = item._type_
        if c_char == array_type:
            return item.value  # bytes
        elif c_wchar == array_type:
            return item.value  # str
        else:
            data = list()
            array_len = len(item)
            for sub_item in item:
                data.append(cvalue_to_dict(sub_item))

            return {item_type_name: data}
    else:
        return item

