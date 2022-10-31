#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2022 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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
__copyright__ = "Copyright © 2012-2022 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "0.0.8"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.file_system.path_manager import path_relative_to_src, RelativePath
from cengal.file_system.directory_manager import current_src_dir
from cengal.file_system.directory_manager import filtered_file_list, FilteringType, filtered_file_list_traversal
from cengal.introspection.inspect import get_exception
from shutil import rmtree
from pprint import pprint
from os import remove
from os.path import splitext


def find_and_prepare_cython_modules(depth = 1):
    depth = depth or 0
    depth += 1
    root = RelativePath(current_src_dir(depth))
    cengal = RelativePath(root('./cengal'))
    cengal_path = cengal('')

    travers_result = filtered_file_list_traversal(cengal_path, FilteringType.off, None, remove_empty_items=True, use_spinner=False)
    for dir_path, dirs, files in travers_result:
        if '__pycache__' in dirs:
            pycache_path = RelativePath(dir_path)('__pycache__')
            try:
                rmtree(pycache_path)
            except OSError as e:
                print(get_exception())

    travers_result = filtered_file_list_traversal(cengal_path, FilteringType.including, {'.pyx', '.c', '.lib', '.dll', '.so'}, remove_empty_items=True, use_spinner=False)
    
    result = list()
    for dir_path, dirs, files in travers_result:
        dir_path_obj = RelativePath(dir_path)
        extensions = dict()
        for file in files:
            filename, file_extension = splitext(file)
            if file_extension not in extensions:
                extensions[file_extension] = set()
            
            extensions[file_extension].add(file)
        
        if '.pyx' in extensions:
            for file_extension, files in extensions.items():
                for file in files:
                    if '.pyx' == file_extension:
                        result.append(dir_path_obj(file))
                    
                    if file_extension in {'.c', '.lib', '.dll', '.so'}:
                        try:
                            remove(dir_path_obj(file))
                        except OSError as e:
                            print(get_exception())
    
    return result
