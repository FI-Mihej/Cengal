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

from cengal.data_manipulation.serialization import *

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

# from cengal.serialization import *
# s = Serializer(Serializers.msgpack)
# data = {1: 'Hello', 2: ('W', 0), 3: ['r', 1, {b'd': '.'}], 'To all!': b'!!1'}
# s.loads(s.dumps(data))


def _single_benchmark(title: str, desired_features: SerializerFeatures, test_data_type: TestDataType):
    print()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~ {} ~~~'.format(title))
    best_serializer, all_results = get_most_efficient_serializers(
            desired_features, test_data_factory(test_data_type))
    output_template = 'Best match: {},\n\nAll results:\n{}'
    print(output_template.format(best_serializer, all_results))


if __name__ == '__main__':
    _single_benchmark('Binary, Small, Single Platform:',
                      {DataFormats.binary, Tags.current_platform},
                      TestDataType.small)
    _single_benchmark('Binary, Small, Multi Platform:',
                      {DataFormats.binary, Tags.multi_platform},
                      TestDataType.small)
    _single_benchmark('Text, Small, Multi Platform:',
                      {DataFormats.text, Tags.multi_platform},
                      TestDataType.small)

    print('\n\n============\n')

    _single_benchmark('Binary, Small, Deep, Single Platform:',
                      {DataFormats.binary, Tags.current_platform},
                      TestDataType.deep_small)
    _single_benchmark('Binary, Small, Deep, Multi Platform:',
                      {DataFormats.binary, Tags.multi_platform},
                      TestDataType.deep_small)
    _single_benchmark('Text, Small, Deep, Multi Platform:',
                      {DataFormats.text, Tags.multi_platform},
                      TestDataType.deep_small)

    print('\n\n============\n')

    _single_benchmark('Binary, Large, Single Platform:',
                      {DataFormats.binary, Tags.current_platform},
                      TestDataType.large)
    _single_benchmark('Binary, Large, Multi Platform:',
                      {DataFormats.binary, Tags.multi_platform},
                      TestDataType.large)
    _single_benchmark('Text, Large, Multi Platform:',
                      {DataFormats.text, Tags.multi_platform},
                      TestDataType.large)

    print('\n\n============\n')

    _single_benchmark('Binary, Large, Deep, Single Platform:',
                      {DataFormats.binary, Tags.current_platform},
                      TestDataType.deep_large)
    _single_benchmark('Binary, Large, Deep, Multi Platform:',
                      {DataFormats.binary, Tags.multi_platform},
                      TestDataType.deep_large)
    _single_benchmark('Text, Large, Deep, Multi Platform:',
                      {DataFormats.text, Tags.multi_platform},
                      TestDataType.deep_large)
