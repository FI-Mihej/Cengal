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

from typing import Dict, List, Union, Set
from .install import *
from cengal.system import IS_INSIDE_OR_FOR_WEB_BROWSER, OS_TYPE
from cengal.hardware.info.cpu import cpu_info


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

        self.linux_allowed: Set[str] = set()
        self.linux_forbidden: Set[str] = set()
        self.windows_allowed: Set[str] = set()
        self.windows_forbidden: Set[str] = set()
        self.osx_allowed: Set[str] = set()
        self.osx_forbidden: Set[str] = set()
        self.emscripten_allowed: Set[str] = set()
        self.emscripten_forbidden: Set[str] = set()

        self.arch__x86__allowed: Set[str] = set()
        self.arch__x86__forbidden: Set[str] = set()
        self.arch__x86_64__allowed: Set[str] = set()
        self.arch__x86_64__forbidden: Set[str] = set()
        self.arch__x86_32__allowed: Set[str] = set()
        self.arch__x86_32__forbidden: Set[str] = set()
        self.arch__ARM__allowed: Set[str] = set()
        self.arch__ARM__forbidden: Set[str] = set()
        self.arch__ARM_8__allowed: Set[str] = set()
        self.arch__ARM_8__forbidden: Set[str] = set()
        self.arch__ARM_8_64__allowed: Set[str] = set()
        self.arch__ARM_8_64__forbidden: Set[str] = set()
        self.arch__ARM_8_32__allowed: Set[str] = set()
        self.arch__ARM_8_32__forbidden: Set[str] = set()
        self.arch__ARM_7__allowed: Set[str] = set()
        self.arch__ARM_7__forbidden: Set[str] = set()

        self._allowed: Set[str] = set()
        self._forbidden: Set[str] = set()

    def chosen_packages(self):
        if IS_INSIDE_OR_FOR_WEB_BROWSER:
            # Must be before other systems!
            self._allowed.update(self.emscripten_allowed)
            self._forbidden.update(self.emscripten_forbidden)
        elif 'Linux' == OS_TYPE:
            self._allowed.update(self.linux_allowed)
            self._forbidden.update(self.linux_forbidden)
        elif 'Windows' == OS_TYPE:
            self._allowed.update(self.windows_allowed)
            self._forbidden.update(self.windows_forbidden)
        elif 'Darwin' == OS_TYPE:
            self._allowed.update(self.osx_allowed)
            self._forbidden.update(self.osx_forbidden)
        
        arch = cpu_info().arch.casefold()
        if cpu_info().is_x86:
            self._allowed.update(self.arch__x86__allowed)
            self._forbidden.update(self.arch__x86__forbidden)
            if 'x86_64'.casefold() == arch:
                self._allowed.update(self.arch__x86_64__allowed)
                self._forbidden.update(self.arch__x86_64__forbidden)
            elif 'x86_32'.casefold() == arch:
                self._allowed.update(self.arch__x86_32__allowed)
                self._forbidden.update(self.arch__x86_32__forbidden)
        
        if cpu_info().is_arm:
            self._allowed.update(self.arch__ARM__allowed)
            self._forbidden.update(self.arch__ARM__forbidden)
            if 'ARM_8'.casefold() == arch:
                self._allowed.update(self.arch__ARM_8__allowed)
                self._forbidden.update(self.arch__ARM_8__forbidden)
            elif ('ARM_8'.casefold() == arch) and (64 == cpu_info().bits):
                self._allowed.update(self.arch__ARM_8_64__allowed)
                self._forbidden.update(self.arch__ARM_8_64__forbidden)
            elif ('ARM_8'.casefold() == arch) and (32 == cpu_info().bits):
                self._allowed.update(self.arch__ARM_8_32__allowed)
                self._forbidden.update(self.arch__ARM_8_32__forbidden)
            elif 'ARM_7'.casefold() == arch:
                self._allowed.update(self.arch__ARM_7__allowed)
                self._forbidden.update(self.arch__ARM_7__forbidden)

        modules = list()
        modules += self.universal
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

        modules.extend(self._allowed)

        if self._forbidden:
            new_modules = list()
            for item in modules:
                if item not in self._forbidden:
                    new_modules.append(item)
            modules = new_modules

        return modules

    def bulk_install(self):
        modules = self.chosen_packages()
        print('INSTALLING: {}'.format(modules))
        print()

        for item in modules:
            install(item, self.list_type)
