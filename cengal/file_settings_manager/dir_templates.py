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


class DirTemplatesManager:
    def __init__(self, templates):
        self._templates = templates

    def make_an_absolute_template(self, root, template_name):
        template_content = self._templates[template_name]
        absolute_template_content = dict()
        for key, data in template_content.items():
            data = data.split(os.path.sep)
            data = os.path.join(root, *data)
            absolute_template_content[key] = data
        return absolute_template_content

    def create_template_in_the_folder(self, root, template_name):
        absolute_template = self.make_an_absolute_template(root, template_name)
        for key, path in absolute_template:
            if not os.path.isdir(path):
                os.makedirs(path)


def get_property_as_relative_dir(config_manager, file, property_name, root):
    property_data = config_manager.get_property(file, property_name)
    property_data = property_data.split(os.path.sep)
    result = os.path.join(root, *property_data)
    return result
