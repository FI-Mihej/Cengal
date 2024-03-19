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


__all__ = ['cli_selector', 'acli_selector']


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.2.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.parallel_execution.asyncio.ainput import ainput

from enum import IntEnum
from typing import Dict, Type, Optional


class CliSelectorTerminatedByUser(Exception):
    pass


def cli_selector(
        variants_type: Type[IntEnum], 
        variant_type_name_per_variant_type: Dict[IntEnum, str], 
        prompt: str,
        default_index: int = 1,
        header: Optional[str] = None, 
        result_template: Optional[str] = None, 
        ):
    if 1 > default_index:
        default_index = 1
    
    variants_num: int = len(variants_type)
    if 1 > variants_num:
        raise ValueError('Empty variants_type')
    
    if default_index > variants_num:
        default_index = variants_num
    
    default_index_str = str(default_index)

    if header is not None:
        print(header)

    for variant_type, variant_type_name in variant_type_name_per_variant_type.items():
        print(f'{variant_type.value}. {variant_type_name}')
    
    result = None
    while not isinstance(result, variants_type):
        try:
            result = variants_type(int((input(prompt)).strip() or default_index_str))
        except ValueError:
            pass  # Try again.
        except KeyboardInterrupt:
            continue  # Control-C pressed. Try again.
        except EOFError:
            raise CliSelectorTerminatedByUser() from None  # Control-D pressed.
    
    if result_template is not None:
        print(result_template.format(result))
    
    return result


async def acli_selector(
        variants_type: Type[IntEnum], 
        variant_type_name_per_variant_type: Dict[IntEnum, str], 
        prompt: str,
        default_index: int = 1,
        header: Optional[str] = None, 
        result_template: Optional[str] = None, 
        ):
    if 1 > default_index:
        default_index = 1
    
    variants_num: int = len(variants_type)
    if 1 > variants_num:
        raise ValueError('Empty variants_type')
    
    if default_index > variants_num:
        default_index = variants_num
    
    default_index_str = str(default_index)

    if header is not None:
        print(header)

    for variant_type, variant_type_name in variant_type_name_per_variant_type.items():
        print(f'{variant_type.value}. {variant_type_name}')
    
    result = None
    while not isinstance(result, variants_type):
        try:
            result = variants_type(int((await ainput(prompt)).strip() or default_index_str))
        except ValueError:
            pass  # Try again.
        except KeyboardInterrupt:
            continue  # Control-C pressed. Try again.
        except EOFError:
            raise CliSelectorTerminatedByUser() from None  # Control-D pressed.
    
    if result_template is not None:
        print(result_template.format(result))
    
    return result
