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


import setuptools
import platform

_PYTHON_VERSION = platform.python_version_tuple()
MODULES_TO_IGNORE = {'cengal._template_module'}
PYTHON_2_MODULES = {'cengal.cross_version.console_print.python2'}


def find_good_packages():
    all_packages = setuptools.find_packages(exclude=['tests', 'tests.*', 'benchmarks', 'benchmarks.*', 'multiproject', 'multiproject.*', 'scripts', 'scripts.*'])
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
    author='TagForest Llc.',
    author_email=__email__,
    description='General purpose library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/FI-Mihej/Cengal',
    license=__license__,
    keywords='general purpose library async loop tools utilities',
    py_modules=['cengal'],
    # package_dir={'': path_relative_to_src('')},
    packages=find_good_packages(),
    setup_requires=pypi_requirements_list,
    install_requires=pypi_requirements_list,
    classifiers=[
        'Programming Language :: Python :: 3',
        f'License :: OSI Approved :: {__license__}',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    ext_modules=cythonize(find_and_prepare_cython_modules(), compiler_directives={'language_level': '3'}),
)
