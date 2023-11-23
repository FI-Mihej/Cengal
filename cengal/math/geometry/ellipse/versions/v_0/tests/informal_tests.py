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


from cengal.math.geometry.ellipse import Ellipse

"""Results for Ellipse(5, 1):
    21.205750411731103
    21.010026651559343
    23.876104167282428
    21.188826246073443
    21.010185796052752
    21.010070798076192
    21.0100598492146
    21.01005354033284
    21.010046444646637
    21.010045234814886
    (21.010044539689165, 533)
    (21.010044539689044, 4096)
"""

"""Results for Ellipse(500, 1):
    1887.3117866440682
    1999.3138980764822
    2356.1976317849985
    2048.179440784419
    2004.993211462262
    2003.847518534776
    2003.5744652543665
    2003.3377375221762
    2002.785086377765
    2002.5086163219212
    (2000.8769360634774, 581)
    (2000.1414074088598, 4096)
"""

el = Ellipse(5, 1)
print(el.perimeter__best_of__euler__and__matt_parker__lazy)
print(el.perimeter__ramanujan_2)
print(el.perimeter__infinite_sum__iter_lim(1))
print(el.perimeter__infinite_sum__iter_lim(10))
print(el.perimeter__infinite_sum__iter_lim(100))
print(el.perimeter__infinite_sum__iter_lim(130))
print(el.perimeter__infinite_sum__iter_lim(140))  # For Ellipse(5, 1): Diviation is similar to perimeter__ramanujan_2 but with opposite sign (perimeter__ramanujan_2 gives number smaller than needed and this gives number greater than needed)
print(el.perimeter__infinite_sum__iter_lim(150))
print(el.perimeter__infinite_sum__iter_lim(180))
print(el.perimeter__infinite_sum__iter_lim(200))
print(el.perimeter__infinite_sum__time_lim(0.100, True))
print(el.perimeter__infinite_sum__time_lim(10.0, True))

