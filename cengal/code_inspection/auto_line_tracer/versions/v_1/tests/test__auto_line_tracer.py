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
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.code_inspection.auto_line_tracer.versions.v_1 import t, tr, tl, ts, te, alt
from unittest import TestCase, main, skip


class TestAutoLineTracer(TestCase):
    # @skip('')
    def test__ts(self):
        ts()
        ts('Hello')
        for _ in range(1):
            k = tr(24 + 15)
            t('Trace Self')
            tl('Trace Next Line')
            k = tr('Hello')
            with alt.different_print_setting(False):
                k = tr('Hello1')
                k = tr('Hello2')
                k = tr('Hello3')
            
            with alt.different_rich_setting(False):
                k = tr('Rich temporary disabled')
            
            k = tr({
                'Hello': 'World!',
                1: 2,
                '3': '4'
            })
        
        te()
        te('World!')

    # @skip('')
    def test__alt_line_str(self):
        print(alt.s())
        print(alt.s('Hello'))
        print(alt.lrs(24 + 15))
        print(alt.nls())
        print(alt.lrs('World'))
        print(alt.lrs({
            'Hello': 'World!',
            1: 2,
            '3': '4'
        }))
        print(alt.e())
        print(alt.e('World!'))


if '__main__' == __name__:
    main()
