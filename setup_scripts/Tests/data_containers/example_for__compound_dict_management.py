#!/usr/bin/env python

# Copyright © 2016 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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

from data_containers.compound_dict_management import *

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2016 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "1.0.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


def test__AddToCompoundDict():
    tagsQnt = {'0': 2, '1': 0, '2': 2, '3': 3, '4': 4, '5': 5}
    tag_hash_set = {'0', '1', '2', '3'}
    tag_by_qnt = dict()
    tag_by_qnt__filler = AddToCompoundDict(
        tag_by_qnt,
        lambda: set(),
        lambda original_dict, key, value: original_dict[key].add(value)
    )
    for tag_hash in tag_hash_set:
        qnt = tagsQnt[tag_hash]
        # if qnt not in tag_by_qnt:
        #     tag_by_qnt[qnt] = set()
        # tag_by_qnt[qnt].add(tag_hash)
        tag_by_qnt__filler.add(qnt, tag_hash)
    print(tag_by_qnt)  # will print '{0: {'1'}, 2: {'0', '2'}, 3: {'3'}}'

    input_items = [0, 2, 3, 5]
    tag_per_item = {
        0: {'red', 'blue'},
        1: {'red'},
        2: {'blue'},
        3: {'orange', 'yellow'},
        4: {'orange'},
        5: {'blue', 'orange', 'yellow'}
    }
    local_tags_qnt = dict()
    local_tags_qnt__filler = AddToCompoundDict(
        local_tags_qnt,
        lambda: 0,
        lambda container, key, value: ResultExistence(True, container[key] + 1)
    )
    for itemID in input_items:
        item_tags = set(tag_per_item[itemID])
        for tag in item_tags:
            # if tag_hash not in local_tags_qnt:
            #     local_tags_qnt[tag_hash] = 0
            # local_tags_qnt[tag_hash] += 1
            local_tags_qnt__filler.add(tag)
    print(local_tags_qnt)  # will print '{'red': 1, 'orange': 2, 'blue': 3, 'yellow': 2}'
