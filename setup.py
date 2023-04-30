#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.1.15"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import setuptools
import platform

_PYTHON_VERSION = platform.python_version_tuple()
MODULES_TO_IGNORE = {'cengal._template_module'}
PYTHON_2_MODULES = {'cengal.cross_version.console_print.python2'}


def find_good_packages():
    all_packages = setuptools.find_packages(exclude=[
            'tests', 'tests.*', 'benchmarks', 'benchmarks.*', 'multiproject', 'multiproject.*', 'scripts', 'scripts.*',
            'cengal.egg-info', 'dist', '.eggs', '.idea', '.vscode',
        ])
    good_packages = list()
    for package in all_packages:
        is_good = True
        for item in MODULES_TO_IGNORE:
            if package.startswith(item):
                is_good = False
                break

        if '3' == _PYTHON_VERSION[0]:
            for item in PYTHON_2_MODULES:
                if package.startswith(item):
                    is_good = False
                    break

        if is_good:
            good_packages.append(package)

    return good_packages


setuptools._install_setup_requires({'setup_requires': ['py-cpuinfo', 'Cython']})


from scripts.install_required_packages.install_packages import install_bundled, get_pypi_requirements_list, get_remote_requirements_list
install_bundled()
from scripts.find_and_prepare_cython_modules import find_and_prepare_cython_modules
from cengal.file_system.path_manager import path_relative_to_src
from Cython.Build import cythonize


with open(path_relative_to_src('README.md'), 'r') as fh:
    long_description = fh.read()

pypi_requirements_list = get_pypi_requirements_list()
remote_requirements_list = get_remote_requirements_list()
setuptools.setup(
    name='cengal',
    version=__version__,
    author=__author__,
    author_email=__email__,
    description='General purpose library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/FI-Mihej/Cengal',
    license=__license__,
    keywords='general purpose library async loop tools utilities bytecode introspection parsing',
    py_modules=['cengal'],
    # package_dir={'': path_relative_to_src('')},
    packages=find_good_packages(),
    setup_requires=pypi_requirements_list,
    install_requires=pypi_requirements_list,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Web Environment',
        'Environment :: WebAssembly',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Telecommunications Industry',
        'Operating System :: Android',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 8',
        'Operating System :: Microsoft :: Windows :: Windows 8.1',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 11',
        'Operating System :: Microsoft :: Windows :: Windows Vista',
        'Operating System :: Microsoft :: Windows :: Windows XP',
        'Operating System :: Microsoft :: Windows :: Windows Server 2008',
        'Operating System :: Microsoft :: Windows :: Windows Server 2003',
        'Operating System :: Microsoft :: Windows :: Windows NT/2000',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: BSD :: OpenBSD',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Operating System :: POSIX :: BSD :: NetBSD',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Operating System :: iOS',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: MicroPython',
        'Topic :: Communications',
        'Topic :: Database',
        'Topic :: Database :: Database Engines/Servers',
        'Topic :: Desktop Environment',
        'Topic :: Games/Entertainment',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Disassemblers',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Testing :: Mocking',
        'Topic :: Software Development :: Testing :: Unit',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: System',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Logging',
        'Topic :: System :: Networking',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: General',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
    python_requires='>=3.7',
    ext_modules=cythonize(find_and_prepare_cython_modules(), compiler_directives={'language_level': '3'}),
)
