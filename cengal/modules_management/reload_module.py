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

import platform
from importlib import import_module
PYTHON_VERSION = platform.python_version_tuple()  # tuple() of str(); for example: ('3', '5', '1')
if PYTHON_VERSION[0] == '2':
    pass
elif PYTHON_VERSION[0] == '3':
    try:
        from imp import reload
    except ImportError:
        from importlib import reload
else:
    raise ImportError()

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


def reload_module(module):
    """
    You SHOULD use construction "import SOME_MODULE" before reload_module() call if construction
        "from SOME_MODULE import SOME_ITEM" was used originally.
    :param module:
    :return:
    """
    reload(module)


def reload_module_by_text_name(module_name, package=None):
    """
    :param module_name: Text representation of module name. "os.path" for example.
        See importlib.import_module() in the Python docs
    :param package: see importlib.import_module() in the Python docs
    :return:
    """
    module = import_module(module_name, package)
    reload(module)
