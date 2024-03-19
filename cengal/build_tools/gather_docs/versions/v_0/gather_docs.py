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


__all__ = [
    'auto_gen', 
    'gather', 
    'merge_docs', 
    'gather_docs', 
]


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.2.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.file_system.directory_manager import FilteringEntity, file_list_traversal, file_list_traversal_ex, ensure_empty_dir, ensure_dir
from cengal.file_system.file_manager import last_ext
from cengal.file_system.path_manager import relative_to_src, get_relative_path_part, RelativePath
from shutil import copyfile
from os.path import join as path_join, dirname, basename
from pprint import pprint
from typing import Any, List, Set, Optional
from pathlib import Path
import shutil

from pdoc import pdoc
from pdoc import render


def auto_gen(repo_root_dir, root_dir, docs_dir, subignore_rel_path: Optional[List[str]] = None):
    subignore_rel_path = subignore_rel_path or list()
    repo_root_dir_rel = RelativePath(repo_root_dir)
    docs_dir_rel = RelativePath(docs_dir)
    src_dir_name = basename(root_dir)
    def py_filter(entity: FilteringEntity, data: Any):
        if FilteringEntity.filename == entity:
            dirpath, filename = data
            if filename in {
                '__init__.py', 
                '_template_submodule.py', 
                '__requirements__.py', 
                '_test__template_submodule.py', 
                '__x__build_config.py', 
                '__build_config.py', 
            }:
                return False
            
            if filename.startswith('test_'):
                return False

            return last_ext(filename) in {'py', 'pyw'}
        elif FilteringEntity.dirname == entity:
            dirpath, dirname = data
            if dirname in {
                '_template_module', 
                '_template_submodule', 
                'compilable', 
                'data', 
                'development', 
                'data', 
                'docs', 
                'tests', 
                'package', 
                'benchmarks', 
                '__pycache__', 
                }:
                return False

            return True
        elif FilteringEntity.dirpath == entity:
            dirpath, dirnames, filenames = data
            dirpath_basename = basename(dirpath)
            if dirpath_basename in {
                '_template_module', 
                '_template_submodule', 
                'compilable', 
                'data', 
                'development', 
                'data', 
                'docs', 
                'tests', 
                'package', 
                'benchmarks', 
                '__pycache__', 
                }:
                return False
            
            return True
        elif FilteringEntity.aggregated == entity:
            return data
        else:
            raise NotImplementedError
    
    subignore = set([repo_root_dir_rel(rel_path) for rel_path in subignore_rel_path])
    result = file_list_traversal_ex(root_dir, py_filter, True, subignore=subignore)
    gen_from_to = dict()
    gen_from = set()
    for dirpath, dirnames, filenames in result:
        for filename in filenames:
            src_path = path_join(dirpath, filename)
            gen_from.add(src_path)
    
    pprint(gen_from)
    dest_root_dir = docs_dir_rel(f'Auto-generated')
    print(dest_root_dir)
    ensure_empty_dir(dest_root_dir)
    out = Path(dest_root_dir)

    template_directory = relative_to_src()('data/pdoc-template')
    # render.configure(template_directory=template_directory)
    render.configure(docformat='markdown', search=False, template_directory=template_directory)
    for src_path in gen_from:
        try:
            print(f'Gen for <{src_path}> into {dest_root_dir}:')
            pdoc(src_path, output_directory=out)
        except:
            pass
    
    print(f'Removing unnecessary files')
    unnecessary_file_names: Set[str] = {
        'index.html',
        'search.js',
    }
    for file_name in unnecessary_file_names:
        full_file_name = out / file_name
        if full_file_name.exists():
            full_file_name.unlink()

    print(f'Renameing from "*.html" to "*.md"')
    for f in out.glob("**/*.html"):
        print(f'\tRenaming <{f}> -> "*.md"')
        f.rename(f.with_suffix(".md"))
    
    print('Done.')


def gather(repo_root_dir, root_dir, docs_dir, subignore_rel_path: Optional[List[str]] = None):
    subignore_rel_path = subignore_rel_path or list()
    repo_root_dir_rel = RelativePath(repo_root_dir)
    docs_dir_rel = RelativePath(docs_dir)
    src_dir_name = basename(root_dir)
    def md_filter(entity: FilteringEntity, data: Any):
        if FilteringEntity.filename == entity:
            dirpath, filename = data
            return 'md' == last_ext(filename)
        elif FilteringEntity.dirname == entity:
            dirpath, dirname = data
            if dirname in {
                '_template_module', 
                '_template_submodule', 
                'tests', 
                '__pycache__', 
                }:
                return False

            return True
        elif FilteringEntity.dirpath == entity:
            dirpath, dirnames, filenames = data
            dirpath_basename = basename(dirpath)
            if dirpath_basename in {
                '_template_module', 
                '_template_submodule', 
                'tests', 
                '__pycache__', 
                }:
                return False
            
            return True
        elif FilteringEntity.aggregated == entity:
            return data
        else:
            raise NotImplementedError
    
    subignore = set([repo_root_dir_rel(rel_path) for rel_path in subignore_rel_path])
    result = file_list_traversal_ex(root_dir, md_filter, True, subignore=subignore)
    copy_from_to = dict()
    for dirpath, dirnames, filenames in result:
        for filename in filenames:
            src_path = path_join(dirpath, filename)
            rel_path_part = get_relative_path_part(dirpath, root_dir)
            dest_path = path_join(src_dir_name, rel_path_part, filename)
            copy_from_to[src_path] = docs_dir_rel(dest_path)
    
    pprint(copy_from_to)
    dest_root_dir = docs_dir_rel(src_dir_name)
    print(dest_root_dir)
    ensure_empty_dir(dest_root_dir)
    for src_path, dest_path in copy_from_to.items():
        print(f'{src_path} -> {dest_path}')
        dest_file_dir = dirname(dest_path)
        print(f'{dest_file_dir}')
        ensure_dir(dest_file_dir)
        copyfile(src_path, dest_path)


def merge_docs(repo_root_dir, root_dir, docs_dir):
    docs_dir_rel = RelativePath(docs_dir)
    src_dir_name = basename(root_dir)
    docs_lib_dir = docs_dir_rel(src_dir_name)
    docs_gen_dir = docs_dir_rel('Auto-generated')
    docs_gen_dir_rel = RelativePath(docs_gen_dir)
    docs_gen_lib_dir = docs_gen_dir_rel(src_dir_name)
    def md_filter(entity: FilteringEntity, data: Any):
        if FilteringEntity.filename == entity:
            dirpath, filename = data
            return 'md' == last_ext(filename)
        elif FilteringEntity.dirname == entity:
            dirpath, dirname = data
            return True
        elif FilteringEntity.dirpath == entity:
            return True
        elif FilteringEntity.aggregated == entity:
            return data
        else:
            raise NotImplementedError
    
    result = file_list_traversal(docs_gen_lib_dir, md_filter, True)
    copy_from_to = dict()
    for dirpath, dirnames, filenames in result:
        for filename in filenames:
            src_path = path_join(dirpath, filename)
            rel_path_part = get_relative_path_part(dirpath, docs_gen_lib_dir)
            dest_path = path_join(src_dir_name, rel_path_part, filename)
            copy_from_to[src_path] = docs_dir_rel(dest_path)
    
    pprint(copy_from_to)
    dest_root_dir = docs_dir_rel(src_dir_name)
    print(dest_root_dir)
    ensure_dir(dest_root_dir)
    for src_path, dest_path in copy_from_to.items():
        print(f'{src_path} -> {dest_path}')
        dest_file_dir = dirname(dest_path)
        print(f'{dest_file_dir}')
        ensure_dir(dest_file_dir)
        copyfile(src_path, dest_path)
    
    print(f'Removing unnecessary generated docs from "{docs_gen_dir}"')
    shutil.rmtree(docs_gen_dir)
    print('Done.')


def gather_docs(repo_root_dir, root_dir, docs_dir, modules_to_ignore: Optional[List[str]] = None):
    auto_gen(repo_root_dir, root_dir, docs_dir, modules_to_ignore)
    gather(repo_root_dir, root_dir, docs_dir, modules_to_ignore)
    merge_docs(repo_root_dir, root_dir, docs_dir)


if '__main__' == __name__:
    cengal_repo_root_dir = relative_to_src()('../../../../..')
    cengal_docs_dir = RelativePath(cengal_repo_root_dir)('docs')
    cengal_src_root_dir = relative_to_src()('../../../..')
    subignore_rel_path = {
        'cengal/_examples', 
        'cengal/_template_module', 
        'cengal/code_flow_control/none_or', 
        'cengal/cross_version/console_print', 
        'cengal/help_tools', 
        'cengal/os/help_tools', 
        'cengal/parallel_execution/coroutines/coro_standard_services/cpu_tick_count_per_second', 
        'cengal/testing_lib', 
        'cengal/text_processing/docten', 
        'cengal/time_management/server_clock', 
        'cengal/universal_parser', 
        'cengal/upk_helping_tools', 
        'cengal/user_interface/console/chooser', 
    }
    auto_gen(cengal_repo_root_dir, cengal_src_root_dir, cengal_docs_dir, subignore_rel_path)
    gather(cengal_repo_root_dir, cengal_src_root_dir, cengal_docs_dir, subignore_rel_path)
    merge_docs(cengal_repo_root_dir, cengal_src_root_dir, cengal_docs_dir)
