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

__all__ = ['plot']

import numpy as np
import matplotlib.pyplot as pyplot
from typing import Optional

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


def plot(amplitude_axis: np.ndarray, title=str(), xlabel=str(), ylabel=str(), psd: bool=False, nfft: Optional[int]=None, samples_per_time_unit: Optional[int]=None):
    time_axis = np.arange(0, len(amplitude_axis))
    if psd:
        pyplot.subplot(211)
    pyplot.plot(time_axis, amplitude_axis)
    pyplot.title(title)
    pyplot.xlabel(xlabel)
    pyplot.ylabel(ylabel)
    pyplot.grid(True, which='both')
    pyplot.axhline(y=0, color='k')
    if psd:
        pyplot.subplot(212)
        pyplot.psd(amplitude_axis, nfft, samples_per_time_unit)
    pyplot.show()
