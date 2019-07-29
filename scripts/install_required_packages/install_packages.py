import sys
import os

from bulk_pip_actions.install import _change_current_dir

import set_environment_variables
set_environment_variables.main()
from bulk_pip_actions.install import *
from bulk_pip_actions.bulk_install import *

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = 'ButenkoMS <gtalk@butenkoms.space>'


class PyPiModules(ModulesLists):
    def __init__(self):
        super(PyPiModules, self).__init__()

        self.list_type = FROM_PYPI

        self.python2 = [
            'paver',  # needed for python-lzf module installation process
            'common-mimetypes',  # for pypy2 and Python2 only
            'python-lzf',  # for pypy2 and Python2 only
        ]

        self.cpython3 = [
        ]

        self.pypy3 = [
        ]

        self.universal = [
            'paver',  # needed for python-lzf module installation process (also for zip-module)
            'requests',  # already preinstalled in Ubuntu 14.04 x64
            'pyOpenSSL',
            'pycurl',  # already preinstalled in Ubuntu 14.04 x64
            'pycrypto',
            'pyasn1',  # already preinstalled in Ubuntu 14.04 x64
            'Jinja2',
            'http-parser',
            'html5lib',  # already preinstalled in Ubuntu 14.04 x64
            'greenlet',
            'Cython',
            'cryptography',  # already preinstalled in Ubuntu 14.04 x64
            'SQLAlchemy',

            'cookies',
            'httpagentparser',
            'python-mimeparse',
            'colorama',
            'httptools',
            'six',
        ]

        self.windows_allowed = {
        }

        self.windows_forbidden = {
        }

        if ((PYTHON_VERSION_INT[0] == 3) and (PYTHON_VERSION_INT[1] < 4)) or (PYTHON_VERSION_INT[0] == 2):
            self.universal.insert(0, 'enum34')  # for pypy3 and Python2 only: it is backport from python34 which is
            #   default in Ubuntu 14.04
            self.universal.insert(0, 'lzmaffi')  # for pypy3 and Python2 only: it is backport from python34 which is
            #   default in Ubuntu 14.04

        if ((PYTHON_VERSION_INT[0] == 3) and (PYTHON_VERSION_INT[1] < 5)) or (PYTHON_VERSION_INT[0] == 2):
            self.universal.insert(0, 'typing')  # for pypy3 and Python2 only: it is backport from python35


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


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    all_modules = [
        PyPiModules(),
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
