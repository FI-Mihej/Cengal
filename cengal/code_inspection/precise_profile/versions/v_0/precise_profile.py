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
    'run', 
    'runctx', 
    'patch', 
    'restore', 
    'PrecisePstats', 
    'precise_pstats', 
    'Stats', 
    'SortKey', 
    'Profile', 
    'profile', 
]


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.time_management.cpu_clock_cycles import perf_counter

from profile import _Utils, Profile as profile_Profile
try:
    from cProfile import Profile as cProfile_cProfile
except ImportError:
    cProfile_cProfile = profile_Profile

from typing import Optional


class _CengalUtils(_Utils):
    def __init__(self, profiler, timer=None):
        super().__init__(profiler)
        self._timer = timer

    def run(self, statement, filename, sort):
        prof = self.profiler(self._timer)
        try:
            prof.run(statement)
        except SystemExit:
            pass
        finally:
            self._show(prof, filename, sort)

    def runctx(self, statement, globals, locals, filename, sort):
        prof = self.profiler(self._timer)
        try:
            prof.runctx(statement, globals, locals)
        except SystemExit:
            pass
        finally:
            self._show(prof, filename, sort)


def run(statement, filename=None, sort=-1, timer=None):
    return _CengalUtils(cProfile_cProfile, perf_counter if timer is None else timer).run(statement, filename, sort)

def runctx(statement, globals, locals, filename=None, sort=-1, timer=None):
    return _CengalUtils(cProfile_cProfile, perf_counter if timer is None else timer).runctx(statement, globals, locals, filename, sort)


def _f8(x):
    return "%8.6f" % x


import pstats
pstats_f8 = pstats.f8
# pstats.f8 = _f8


def patch():
    pstats.f8 = _f8


def restore():
    pstats.f8 = pstats_f8


class PrecisePstats:
    def __init__(self):
        self.f8 = pstats.f8

    def __enter__(self):
        pstats.f8 = _f8
        return Stats

    def __exit__(self, exc_type, exc_val, exc_tb):
        pstats.f8 = self.f8


precise_pstats = PrecisePstats


from pstats import Stats, SortKey


class Profile:
    """Will run profile on the statement, save the results to the temp-file and return the Stats object. Will also delete the temp-file on exit or on exception.

    Example:
        ```python
        with Profile('from cengal_import_test import importing_time') as p:
            p.sort_stats('cumulative').print_stats()
        ```
    """    
    def __init__(self, statement, filename: Optional[str] = None, sort=-1, timer=None, app_name: Optional[str] = None) -> None:
        self._statement = statement
        self._filename: str = filename
        self._sort = sort
        self._timer = timer
        self._app_name: str = app_name
        self._precise_pstats = PrecisePstats()
    
    def __enter__(self):
        if not self._filename:
            from cengal.file_system.file_manager import gen_random_file_path
            from cengal.file_system.app_fs_structure.app_dir_path import  AppDirectoryType, adp
            temp_dir_name: str = adp(AppDirectoryType.local_temp, self._app_name if self._app_name else 'cengal.precise_profile', with_structure=True, ensure_dir=True)
            self._filename = gen_random_file_path(temp_dir_name, 'profile_', 'prof')
        
    
        from cengal.code_flow_control.exception_to_warning import exception_to_warning
        with exception_to_warning():
            run(self._statement, self._filename, self._sort, self._timer)

        self._precise_pstats.__enter__()
        return Stats(self._filename)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._precise_pstats.__exit__(exc_type, exc_val, exc_tb)
        self._remove_file()
    
    def _remove_file(self):
        if self._filename:
            from cengal.file_system.file_manager import file_exists
            if file_exists(self._filename):
                from os import remove
                remove(self._filename)
            
            self._filename = None


def profile(statement, filename: Optional[str] = None, sort=-1, timer=None, app_name: Optional[str] = None) -> Stats:
    """Will run profile on the statement, save the results to the temp-file and return the Stats object.

    Example:
        ```python
        with precise_pstats():
            profile('from cengal_import_test import importing_time').sort_stats('cumulative').print_stats()
        ```

        or

        ```python
        with precise_pstats():
            p: Stats = profile('from cengal_import_test import importing_time')
            p.sort_stats('cumulative').print_stats()
        ```

    Args:
        statement (_type_): _description_
        filename (_type_, optional): _description_. Defaults to None.
        sort (int, optional): _description_. Defaults to -1.
        timer (_type_, optional): _description_. Defaults to None.
        app_name (Optional[str], optional): _description_. Defaults to None.

    Returns:
        Stats: _description_
    """    
    if not filename:
        from cengal.file_system.file_manager import gen_random_file_path
        from cengal.file_system.app_fs_structure.app_dir_path import  AppDirectoryType, adp
        temp_dir_name: str = adp.cached(AppDirectoryType.local_temp, app_name if app_name else 'cengal.precise_profile', with_structure=True, ensure_dir=True)
        filename = gen_random_file_path(temp_dir_name, 'profile_', 'prof')
        print(filename)
    
    from cengal.code_flow_control.exception_to_warning import exception_to_warning
    with exception_to_warning():
        run(statement, filename, sort=sort, timer=timer)

    return Stats(filename)
