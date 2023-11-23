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


__all__ = ['main']

import sys
import os

# from cengal.bulk_pip_actions.install import _change_current_dir

# import set_environment_variables
#
# set_environment_variables.main()
from cengal.bulk_pip_actions.install import *
from cengal.bulk_pip_actions.bulk_install import *
from typing import List



__author__ = 'ButenkoMS <gtalk@butenkoms.space>'


class PyPiModules(ModulesLists):
    def __init__(self):
        super(PyPiModules, self).__init__()

        self.list_type = FROM_PYPI

        self.python2 = [
            'paver',  # needed for python-lzf module installation process
            'common-mimetypes',  # for pypy2 and Python2 only
            'python-lzf',  # for pypy2 and Python2 only
            # 'line-profiler',  # for CPython only! (as far as I know)
            # 'macropy',

            # ==================
            # OPTIONAL PACKAGES:
        ]

        self.cpython2 = [
            # 'macropy',

            # ==================
            # OPTIONAL PACKAGES:
        ]

        self.cpython3 = [
            # 'macropy3',

            # ==================
            # OPTIONAL PACKAGES:
        ]

        self.pypy2 = [
            # 'macropy',

            # ==================
            # OPTIONAL PACKAGES:
            'msgpack-pypy',
        ]

        self.pypy3 = [
            # 'macropy3',

            # ==================
            # OPTIONAL PACKAGES:
            'msgpack-pypy',
        ]

        self.universal = [
            # 'wheel',
            # 'virtualenv',

            'Cython>=0.29.34',
            'python-dateutil',
            # 'holidays',
            # 'bdateutil',  # Used by Cengal. However requires outdated version of python-dateutil==2.2. Leads to conflicts with 'pendulum' and 'pandas'. Must not be installed. Latest dev version will be installed from github in ExternalGitModules.

            # 'paver',  # needed for python-lzf module installation process (also for zip-module)
            # 'urllib3',  # already preinstalled in Ubuntu 14.04 x64
            # 'thrift',
            # 'thriftpy',
            # 'tornado',
            'requests',  # already preinstalled in Ubuntu 14.04 x64
            # 'pyOpenSSL',
            # 'pycurl',  # already preinstalled in Ubuntu 14.04 x64
            # 'pycrypto',  # outdated. Would not install on Windows easily
            # 'http-parser',
            # 'html5lib',  # already preinstalled in Ubuntu 14.04 x64
            'greenlet',
            # 'cryptography',  # already preinstalled in Ubuntu 14.04 x64
            # 'SQLAlchemy',

            # 'audioread',
            # 'beautifulsoup4',
            # 'cchardet',
            # 'charset_normalizer',
            # 'cookies',
            # 'decorator',
            # 'httpagentparser',
            # 'pyaudio',  # a bit outdated. Would not install on Windows easily
            # 'pygeoip',
            # 'pylast',
            # 'python-mimeparse',
            'colorama',
            # 'bintrees',
            # 'python-Levenshtein',
            # 'httptools',  # Used in tests and benchmarks
            # 'six',

            # 'psycopg2',

            # 'pyinstaller',
            # 'pywin32',  # Would not install on Windows easily. MSI package should be used

            'py-cpuinfo',
            # 'pypreprocessor',
            # 'conditional',

            # 'rocksdb',
            'lmdb',

            # 'json2html',
            # 'json2table',

            # 'Flask',
            # 'MarkupSafe',
            # 'itsdangerous',
            # 'Jinja2',

            'async_generator',
            # 'dependable',  # just interesting package. Was found while searching PyPi for an async_generator package
            # 'janus',
            
            # 'distex',
            
            # 'version',  # https://github.com/keleshev/version Interesting. Python 3 unsupported however. Fixed version from https://github.com/YouCannotBurnMyShadow/version.git should be used instead

            # ==================
            # OPTIONAL PACKAGES:
            'simplejson',
            # 'pyasn1',  # already preinstalled in Ubuntu 14.04 x64
            'cbor',
            'cbor2',
            'ujson',
            'orjson',
            'cloudpickle',
            'python3-dtls',
            'psutil',
            'ttkbootstrap',
            'pprintpp'
        ]

        # self.windows_allowed = {
        #     # 'pyinstaller',
        #     # 'pywin32',
        # }

        self.windows_forbidden = {
            'virtualenv',
            'rocksdb',
            'distex',
        }

        self.osx_allowed = {
            'pyobjc'
        }

        self.emscripten_forbidden = {
            'virtualenv',
            'rocksdb',
            'distex',
            'requests',  # already preinstalled in Ubuntu 14.04 x64
            'greenlet',
            'lmdb',
            'ttkbootstrap'
        }

        if (PYTHON_VERSION_INT[:3] < (3, 4, 0)):
            self.universal.insert(0, 'enum34')  # for pypy3 and Python2 only: it is backport from python34 which is
            #   default in Ubuntu 14.04
        
        if ('CPython'.lower() == PLATFORM_NAME.lower()) and (PYTHON_VERSION_INT[:3] < (3, 3, 0)):
            self.universal.insert(0, 'lzmaffi')  # for pypy3 and Python2 only: it is backport from python34 which is
            #   default in Ubuntu 14.04
        
        if ('PyPy'.lower() == PLATFORM_NAME.lower()) and (PYTHON_VERSION_INT[:3] < (3, 4, 0)):
            self.universal.insert(0, 'lzmaffi')  # for pypy3 and Python2 only: it is backport from python34 which is
            #   default in Ubuntu 14.04

        if (PYTHON_VERSION_INT[:3] < (3, 5, 0)):
            self.universal.insert(0, 'typing')  # for pypy3 and Python2 only: it is backport from python35
        
        if (PYTHON_VERSION_INT[:3] < (3, 8, 0)):
            self.cpython2.insert(0, 'msgpack-python')
            self.cpython3.insert(0, 'msgpack-python')
        
        if (PYTHON_VERSION_INT[:3] >= (3, 8, 0)):
            self.cpython2.insert(0, 'msgpack')
            self.cpython3.insert(0, 'msgpack')
        
        if (PYTHON_VERSION_INT[:3] < (3, 11, 1)):
            self.universal.insert(0, 'cchardet')  # 2023.01.27: 3.11.1 is not supported yet: error: longintrepr.h: No such file or directory
            self.universal.insert(0, 'http-parser')  # 2023.01.27: 3.11.1 is not supported yet: error: longintrepr.h: No such file or directory
        
        if (PYTHON_VERSION_INT[:3] < (3, 13, 0)):
            self.universal.insert(0, 'charset_normalizer')  # 2023.11.16: 3.12 is declared to be supported. Testing required
        
        if (PYTHON_VERSION_INT[:3] >= (3, 12, 0)):
            self.windows_allowed.add('patch-ng')  # `Exception: Building py-lmdb from source on Windows requires the "patch-ng" python module.`. 2023.11.18: py-lmdb does not support 3.12 yet. Testing required
            self._forbidden.add('lmdb')  # 2023.11.21: There is no wheels for pypy3.12 and above.
        
        if 'PyPy'.lower() == PLATFORM_NAME.lower():
            if (PYTHON_VERSION_INT[:2] == (3, 10)):
                self.windows_forbidden.add('lmdb')  # 2023.11.21: There is no wheels for pypy3.9 on Windows.

            if (PYTHON_VERSION_INT[:2] != (3, 9)) and (PYTHON_VERSION_INT[:2] != (2, 7)):
                self.windows_allowed.add('patch-ng')  # 2023.11.21: There is only wheels for pypy2.7 and pypy3.9 on Windows

            if (PYTHON_VERSION_INT[:2] != (2, 7)):
                self.osx_allowed.add('patch-ng')  # 2023.11.21: There is only wheel for pypy2.7 on OSX
            
            self._forbidden.add('orjson')  # 2023.11.21: There is no wheels for PyPy on Windows. And for build it requires Rust build tools to be installed
            self.arch__ARM__allowed.add('patch-ng')  # 2023.11.21: There is no prebuilt wheel for ARM
            self.windows_forbidden.add('psutil')  # 2023.11.21: It won't compile under PyPy3.9 or PyPy3.10 on Windows


class ExternalGitModules(ModulesLists):
    def __init__(self):
        super(ExternalGitModules, self).__init__()

        self.list_type = FROM_EXTERNAL_GIT

        self.universal = [
            # 'git+https://github.com/Epikem/pypreprocessor.git',  # temporary workaround for pypreprocessor: https://github.com/interpreters/pypreprocessor/pull/15 . https://github.com/YouCannotBurnMyShadow/pypreprocessor.git must be used instead:
            # 'git+https://github.com/YouCannotBurnMyShadow/pypreprocessor.git',
            'git+https://github.com/YouCannotBurnMyShadow/python-bdateutil.git',  # TODO: check is it really will be installed
            'git+https://github.com/YouCannotBurnMyShadow/version.git',  # TODO: check is it really will be installed
            'git+https://github.com/FI-Mihej/fi-patched--progress.git',  # TODO: check is it really will be installed
        ]

        self.arch__x86_64__allowed = {
        }

        self.arch__x86_32__allowed = {
        }

        self.emscripten_forbidden = {
            'git+https://github.com/FI-Mihej/fi-patched--progress.git',
        }



class ZipModules(ModulesLists):
    def __init__(self):
        super(ZipModules, self).__init__()

        self.list_type = FROM_ZIP


class FoldersWithZippedModules(ModulesLists):
    def __init__(self):
        super(FoldersWithZippedModules, self).__init__()

        self.list_type = FROM_FOLDER_WITH_ZIP_FILES

        dir_of_the_current_file = os.path.dirname(os.path.abspath(__file__))

        self.python3 = [
            os.path.join(dir_of_the_current_file, 'InstallSources', 'Python', 'Packets', 'Python3')
        ]

        self.universal = [
            os.path.join(dir_of_the_current_file, 'InstallSources', 'Python', 'Packets', 'Universal')
        ]


def install_bundled(args=None):
    if args is None:
        args = sys.argv[1:]

    all_modules = [
        ExternalGitModules(),
        ZipModules(),
        FoldersWithZippedModules(),
    ]

    for modules_bunch in all_modules:
        modules_bunch.bulk_install()

    return 0


def get_pypi_requirements_list() -> List[str]:
    pypi_modules: PyPiModules = PyPiModules()
    return pypi_modules.chosen_packages()


def get_remote_requirements_list() -> List[str]:
    result: List[str] = list()
    pypi_modules: PyPiModules = PyPiModules()
    result.extend(pypi_modules.chosen_packages())
    external_git_modules = ExternalGitModules()
    result.extend(external_git_modules.chosen_packages())
    return result


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    all_modules: List[ModulesLists] = [
        PyPiModules(),
        ExternalGitModules(),
        ZipModules(),
        FoldersWithZippedModules(),
    ]

    # path_to_interpreter = os.path.dirname(sys.executable)
    # sys.path.append(path_to_interpreter)
    # with _change_current_dir(path_to_interpreter):
    #     for modules_bunch in all_modules:
    #         modules_bunch.bulk_install()
    for modules_bunch in all_modules:
        modules_bunch.bulk_install()

    return 0


if __name__ == '__main__':
    sys.exit(main())
