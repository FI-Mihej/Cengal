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

import os.path
from os.path import expanduser
from cengal.text_processing import get_text_in_brackets
import copy
from enum import Enum
from contextlib import contextmanager

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


# RESERVED_SYMBOLS__NAME = {'"', '='}
RESERVED_SYMBOLS__NAME = {'"'}
RESERVED_SYMBOLS__DATA = {'\n'}
RESERVED_SYMBOLS = RESERVED_SYMBOLS__NAME | RESERVED_SYMBOLS__DATA


class WrongSymbolInThePropertyName(Exception):
    pass


class WrongSymbolInThePropertyData(Exception):
    pass


class Errors(Enum):
    ok = 0
    file_not_found = 1


class ConfigManager:
    def __init__(self, app_tags, base_dir=None, default_content=None, immediate_save=True):
        """
        :param app_tags: ['Cute LLC', 'My App Name', 'configs for a parser']
        :param base_dir: User's Home if None
        :param immediate_save:
        :return:
        """
        self.app_tags = app_tags
        self.base_dir = base_dir or os.path.expanduser("~")
        self.config_path = os.path.join(self.base_dir, *self.app_tags)
        if not os.path.isdir(self.config_path):
            os.makedirs(self.config_path)
        self.default_content = default_content
        self.immediate_save = immediate_save

        self.files = dict()

        self.predefined_file_name = None

    @staticmethod
    def _filter_out_disallowed_symbols_from_property_name(property_name):
        for disallowed in RESERVED_SYMBOLS__NAME:
            property_name = property_name.replace(disallowed, '')
        return property_name

    def get_full_dir_path(self):
        return copy.copy(self.config_path)

    def load(self, file_name, force=None):
        if self.predefined_file_name is not None:
            force = file_name
            file_name = self.predefined_file_name
        # elif force is None:
        #     raise Exception('"force" property must be provided!')

        if force is None:
            force = False

        result = Errors.ok
        file_content = self.files.get(file_name)
        if (file_content is None) or force:
            # file_content = None
            file_path = os.path.join(self.config_path, file_name)
            file_lines = list()
            try:
                with open(file_path, 'r') as file:
                    file_lines = file.readlines()
            except FileNotFoundError as ex:
                result = Errors.file_not_found
            file_content = dict()
            for another_line in file_lines:
                another_line += '\n'
                key = get_text_in_brackets(another_line, '"', '"').strip()
                data = get_text_in_brackets(another_line, '=', '\n').strip()
                file_content[key] = data
            if file_name in self.default_content:
                file_default_content = self.default_content[file_name]
                for key, data in file_default_content.items():
                    if key not in file_content:
                        file_content[key] = data
            self.files[file_name] = file_content
            self.save(file_name)
        return result

    def save(self, file_name=None):
        if self.predefined_file_name is not None:
            file_name = self.predefined_file_name
        elif file_name is None:
            raise Exception('"file_name" property must be provided!')

        file_content = self.files.get(file_name)
        if file_content is not None:
            lines = list()
            for key, data in file_content.items():
                another_line = '"{}" = {}'.format(key, data)
                lines.append(another_line)
            new_file_content = '\n'.join(lines)
            file_path = os.path.join(self.config_path, file_name)
            with open(file_path, 'w') as file:
                file.write(new_file_content)

    def get_property(self, file_name, property_name=None):
        if self.predefined_file_name is not None:
            property_name = file_name
            file_name = self.predefined_file_name
        elif property_name is None:
            raise Exception('"property_name" property must be provided!')

        result = None
        self.load(file_name)
        file_content = self.files[file_name]
        property_name = self._filter_out_disallowed_symbols_from_property_name(property_name)
        result = copy.deepcopy(file_content.get(property_name))
        return result

    def set_property(self, file_name, property_name, data=None):
        """
        :param file_name:
        :param property_name:
        :param data: set to None to remove property from config
        :return:
        """

        if self.predefined_file_name is not None:
            data = property_name
            property_name = file_name
            file_name = self.predefined_file_name
        elif data is None:
            raise Exception('"data" property must be provided!')

        data = copy.deepcopy(data)
        self.load(file_name)
        file_content = self.files[file_name]
        if data is None:
            if property_name in file_content:
                del file_content[property_name]
        else:
            for disallowed in RESERVED_SYMBOLS__DATA:
                if disallowed in data:
                    raise WrongSymbolInThePropertyData(data)
            property_name = self._filter_out_disallowed_symbols_from_property_name(property_name)
            file_content[property_name] = copy.copy(data)
        if self.immediate_save:
            self.save(file_name)

    def remove_property(self, file_name, property_name=None):
        if self.predefined_file_name is not None:
            property_name = file_name
            file_name = self.predefined_file_name
        elif property_name is None:
            raise Exception('"property_name" property must be provided!')

        self.set_property(file_name, property_name, None)


@contextmanager
def conf_file_name(config_manager: ConfigManager, file_name: str):
    original_file_name = config_manager.predefined_file_name
    config_manager.predefined_file_name = file_name
    try:
        yield config_manager
    finally:
        config_manager.predefined_file_name = original_file_name
