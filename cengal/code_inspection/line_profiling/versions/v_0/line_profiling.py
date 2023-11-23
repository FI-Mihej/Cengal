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

from contextlib import contextmanager
from cengal.code_flow_control.smart_values.versions.v_0 import ResultExistence
from cengal.system import PYTHON_VERSION_INT

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


class DumbProfiler:
    def __call__(self, function):
        return function

    def print_stats(self):
        return

    def dump_stats(self):
        return


try:
    from line_profiler import LineProfiler
except ImportError:
    LineProfiler = DumbProfiler


def set_profiler(allow_profiling=True):
    prof = None
    if allow_profiling:
        prof = LineProfiler()
    else:
        prof = DumbProfiler()
    if PYTHON_VERSION_INT[0] >= 3:
        import builtins
    else:
        import __builtin__ as builtins
    if 'profile' not in builtins.__dict__:
        builtins.__dict__['profile'] = prof
    else:
        if type(builtins.__dict__['profile']) != type(prof):
            raise Exception('Profiler settings are desynced between modules!')


@contextmanager
def profiler_result(profiler, print_result=False, output_file: ResultExistence=None):
    output_file = output_file or ResultExistence(None, None)

    try:
        yield profiler
    except:
        raise
    finally:
        if print_result:
            profiler.print_stats()
        if output_file.existence:
            if output_file.result:
                profiler.dump_stats(output_file.result)
            else:
                # TODO: сделать автоматическое имя из имени прогоняемого файла и случайного GUID
                raise NotImplemented()


