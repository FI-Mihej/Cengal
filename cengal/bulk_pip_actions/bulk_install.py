#!/usr/bin/env python
# coding=utf-8

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

from .install import *
import os

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


class ModulesLists(object):
    def __init__(self):
        self.list_type = None

        self.python2 = list()
        self.python3 = list()
        self.cpython2 = list()
        self.cpython3 = list()
        self.pypy2 = list()
        self.pypy3 = list()
        self.universal = list()

        self.linux_allowed = None
        self.linux_forbidden = None
        self.windows_allowed = None
        self.windows_forbidden = None
        self.osx_allowed = None
        self.osx_forbidden = None

        self._allowed = None
        self._forbidden = None

        if 'posix' == os.name:
            self._allowed = self.linux_allowed
            self._forbidden = self.linux_forbidden
        elif 'nt' == os.name:
            self._allowed = self.windows_allowed
            self._forbidden = self.windows_forbidden
        elif 'mac' == os.name:
            self._allowed = self.osx_allowed
            self._forbidden = self.osx_forbidden

    def bulk_install(self):
        modules = list()
        if '2' == PYTHON_VERSION[0]:
            if 'CPython' == PLATFORM_NAME:
                modules += self.cpython2
            elif 'PyPy' == PLATFORM_NAME:
                modules += self.pypy2
            modules += self.python2
        if '3' == PYTHON_VERSION[0]:
            if 'CPython' == PLATFORM_NAME:
                modules += self.cpython3
            elif 'PyPy' == PLATFORM_NAME:
                modules += self.pypy3
            modules += self.python3
        modules += self.universal

        if self._allowed is not None:
            new_modules = list()
            for item in modules:
                if item in self._allowed:
                    new_modules.append(item)
            modules = new_modules

        if self._forbidden is not None:
            new_modules = list()
            for item in modules:
                if item not in self._forbidden:
                    new_modules.append(item)
            modules = new_modules

        print('INSTALLING: {}'.format(modules))
        print()

        for item in modules:
            install(item, self.list_type)
