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


from os import environ
if 'CENGAL_BUILD_IS_IN_DEBUG_MODE' in environ:
    import debugpy
    debugpy.listen(("0.0.0.0", 5678))
    debugpy.wait_for_client()
    debugpy.breakpoint()


environ['CENGAL_IS_IN_BUILD_MODE'] = 'True'


import setuptools
# from setuptools import Extension, setup
# import platform


setuptools._install_setup_requires({'setup_requires': ['Cython>=0.29.34', 'py-cpuinfo', 'charset-normalizer; python_version < "3.13"']})

from cengal_setup_scripts.install_required_packages.install_packages import install_bundled, get_pypi_requirements_list, get_remote_requirements_list
# install_bundled()
from cengal_setup_scripts.find_and_prepare_cython_modules import find_and_prepare_cython_modules, build, build_ext, sdist, \
    find_good_packages, find_package_data
from cengal.file_system.path_manager import path_relative_to_src


with open(path_relative_to_src('README.md'), 'r') as fh:
    long_description = fh.read()

setup_requires = [
    "charset-normalizer; python_version < '3.13'", 
    "chardet; python_version < '3.11'",
    "py-cpuinfo",
    "Cython>=0.29.34",
    "patch-ng; python_version >= '3.12' or (platform_python_implementation == 'PyPy' and platform_system == 'Windows')",
]
pypi_requirements_list = get_pypi_requirements_list()
if 'patch-ng' in pypi_requirements_list:
    pypi_requirements_list.remove('patch-ng')
    pypi_requirements_list.insert(0, 'patch-ng')
    
remote_requirements_list = get_remote_requirements_list()


from cengal.system import CENGAL_IS_IN_BUILD_MODE
from cengal.build_tools.current_compiler import compiler_type
from cengal.build_tools.prepare_cflags import prepare_cflags, concat_cflags, prepare_compile_time_env


prepare_cflags({
    'CENGAL_IS_IN_BUILD_MODE': (False, CENGAL_IS_IN_BUILD_MODE),
    'CENGAL_BUILD_IS_IN_DEBUG_MODE': (False, 'CENGAL_BUILD_IS_IN_DEBUG_MODE' in environ),
})


if 'CENGAL_BUILD_IS_IN_DEBUG_MODE' in environ:
    debugpy.breakpoint()


packages_data_dict, manifest_included_files = find_package_data()
setuptools.setup(
    name='cengal',
    version=__version__,
    author='ButenkoMS',
    author_email=__email__,
    description='General purpose library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/FI-Mihej/Cengal',
    license=__license__,
    keywords='async loop, coroutine, async wxPython, async Qt, async Tkinter, bytecode manipulation, introspection, text parsing',
    py_modules=['cengal'],
    # package_dir={'': path_relative_to_src('')},
    packages=find_good_packages(),
    package_data=packages_data_dict,
    setup_requires=setup_requires,
    install_requires=pypi_requirements_list,
    # extras_require={
    #     'hardware__info__cpu__versions__v_1': ['py-cpuinfo'],
    # },
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
        'Programming Language :: C',
        'Programming Language :: Cython',
        'Programming Language :: Python',
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
        'Topic :: Database :: Front-Ends',
        'Topic :: Database :: Database Engines/Servers',
        'Topic :: Desktop Environment',
        'Topic :: Games/Entertainment',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Page Counters',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Wiki',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development',
        'Topic :: Software Development :: Assemblers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Disassemblers',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Interpreters',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization',
        'Topic :: Software Development :: Object Brokering',
        'Topic :: Software Development :: Pre-processors',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Testing :: Mocking',
        'Topic :: Software Development :: Testing :: Unit',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: Software Development :: Widget Sets',
        'Topic :: System',
        'Topic :: System :: Benchmark',
        'Topic :: System :: Clustering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Filesystems',
        'Topic :: System :: Hardware',
        'Topic :: System :: Hardware :: Symmetric Multi-processing',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: System :: Networking :: Monitoring :: Hardware Watchdog',
        'Topic :: System :: Shells',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Text Processing :: Markup',
        'Topic :: Utilities',
        'Typing :: Typed',
        # 'Private :: Do Not Upload',
    ],
    python_requires='>=3.8',
    ext_modules=find_and_prepare_cython_modules(),
    # ext_modules=cythonize(
    #     find_and_prepare_cython_modules(),
    #     compiler_directives={'language_level': '3'},
    #     compile_time_env = prepare_compile_time_env(),
    # ),
    cmdclass={
        # 'build_ext': build_ext,
        'build': build,
        'sdist': sdist,
    },
)
