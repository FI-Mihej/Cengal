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


from cengal.math.numbers import RationalNumber
from cengal.data_manipulation.conversion.bit_cast_like import bit_cast__uint32_to_float, bit_cast__float_to_uint32


def rsqrt(x: RationalNumber) -> float:
    """Fast inverse square root
    https://en.wikipedia.org/wiki/Fast_inverse_square_root

    Args:
        x (RationalNumber): _description_

    Returns:
        float: _description_
    """
    if isinstance(x, int):
        x = float(x)
    
    y = bit_cast__uint32_to_float(0x5f3759df - (bit_cast__float_to_uint32(x) >> 1))
    return y * (1.5 - (x * 0.5 * y * y))
