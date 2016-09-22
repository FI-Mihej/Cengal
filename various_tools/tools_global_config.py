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

from file_settings_manager.config_manager import *

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


class KnownExternalEditors(ConfigManager):
    def __init__(self, immediate_save=True):
        default_content = {
            'known external editors': {
                'list of known editors': '["pycharm", "visual studio code"]',
                'default editor': 'visual studio code',
                'path to pycharm exe': '',
                'pycharm cmd template': '"%exe%" "%file%"',
                'path to visual studio code exe': '',
                'visual studio code cmd template': '"%exe%" -g "%file%":%line%:0'
            },
        }
        super(KnownExternalEditors, self).__init__(['.PythonLibs Settings', 'Various Tools'],
                                                   default_content=default_content,
                                                   immediate_save=immediate_save)
