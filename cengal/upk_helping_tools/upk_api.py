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

from cengal.web_tools.request_cache import RequestCache
from cengal.text_processing import get_text_in_brackets
from cengal.data_manipulation import hex_dword_to_int, get_slice_from_array, bytes__to__hex_string
from cengal.code_flow_control.chained_flow.versions.v_1.chained_flow import Chain, link, chain_reader, \
    ResultType, CriteriaType
from cengal.upk_helping_tools.upk_constants import FileExtensions, UpkHexFilesInternals

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


def get_function_bytecode_by_name(full_function_path,
                                  upk_utils_dir,
                                  xcom_unpacked_upk_dir,
                                  xcom_deserialized_upk_dir,
                                  output_dir,
                                  cache=None):
    """
    :param full_function_path: "filename without ext"+"class name"+"function name";
     example: 'XComGame.XGAbility_Targeted.CalcDamage'
    :param upk_utils_dir:
    :param xcom_unpacked_upk_dir:
    :param xcom_deserialized_upk_dir:
    :param output_dir:
    :param cache:
    :return:
    """

    cache = cache or RequestCache(2)

    pass
