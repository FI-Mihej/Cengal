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
__version__ = "4.3.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import hashlib
import os
import shutil
import sys
import zipfile
from pathlib import Path

def sha256_checksum(filename):
    with open(filename, 'rb') as f:
        bytes = f.read()  # Read file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest()
    return readable_hash

def update_wheel(package_name, target_python_version, python_interpreter, python_version, python_abi, target_os, target_architecture, target_os_and_arghitecture, wheel_path: Path):
    wheel_path_str = str(wheel_path)
    print(f"Updating wheel: {wheel_path_str}")
    curdir = Path.cwd()
    try:
        unpacked_dir = Path(curdir) / 'unpacked_wheel'
        if unpacked_dir.exists():
            shutil.rmtree(unpacked_dir)
        
        unpacked_dir.mkdir()

        # Unzip the wheel
        with zipfile.ZipFile(wheel_path_str, 'r') as zip_ref:
            zip_ref.extractall(unpacked_dir)

        # Add BUILD_INFO.txt
        dist_info_dirs = list(unpacked_dir.glob(f'{package_name}-*.dist-info'))
        if not dist_info_dirs:
            print(f"\tNo dist-info directory found for {package_name}", file=sys.stderr)
            return

        build_info_path = dist_info_dirs[0] / 'BUILD_INFO.txt'
        with open(build_info_path, 'w') as f:
            f.write(f"Python Interpreter: {python_interpreter}\n")
            f.write(f"Python Version: {python_version}\n")
            f.write(f"Target OS: {target_os}\n")
            f.write(f"Target Architecture: {target_architecture}\n")

        # Update RECORD file
        record_path = dist_info_dirs[0] / 'RECORD'
        with open(record_path, 'a') as record_file:
            build_info_path_str = str(build_info_path)
            hash = sha256_checksum(build_info_path_str)
            size = build_info_path.stat().st_size
            relative_path = str(build_info_path.relative_to(unpacked_dir))
            record_file.write(f"{relative_path},sha256={hash},{size}\n")
        
        # Update 'Tag' in WHEEL file
        sdist_wheel_path = dist_info_dirs[0] / 'WHEEL'
        with open(sdist_wheel_path, 'r') as f:
            lines = f.readlines()
        
        with open(sdist_wheel_path, 'w') as f:
            for line in lines:
                if line.startswith('Tag:'):
                    f.write(f"Tag: {target_python_version}-{python_abi}-{target_os_and_arghitecture}\n")
                else:
                    f.write(line)
        
        # Find existing record and update WHEEL file hash in RECORD file
        sdist_wheel_path_str = str(sdist_wheel_path)
        hash = sha256_checksum(sdist_wheel_path_str)
        size = sdist_wheel_path.stat().st_size
        relative_path = str(sdist_wheel_path.relative_to(unpacked_dir))
        with open(record_path, 'r') as f:
            lines = f.readlines()
        
        new_lines = list()
        for line in lines:
            if line.startswith(relative_path):
                new_lines.append(f"{relative_path},sha256={hash},{size}\n")
            else:
                new_lines.append(line)
        
        new_content = ''.join(new_lines)
        with open(record_path, 'w') as f:
            f.write(new_content)

        # Repackage the wheel
        print(f"\tRepackaging wheel: {wheel_path_str}")
        os.remove(wheel_path_str)
        with zipfile.ZipFile(wheel_path_str, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
            for file in unpacked_dir.rglob('*'):
                zipf.write(file, file.relative_to(unpacked_dir))

        shutil.rmtree(unpacked_dir)
        print(f"Updated wheel saved to: {wheel_path_str}")
    finally:
        os.chdir(curdir)


def update_wheels():
    curdir = Path.cwd()
    try:
        wheelhouse_dir = Path(curdir) / 'wheelhouse'
        print(wheelhouse_dir)
        if not wheelhouse_dir.exists():
            wheelhouse_dir.mkdir()
        
        os.chdir(wheelhouse_dir)
        for whl_file in wheelhouse_dir.glob(f'cengal*.whl'):
            wheel_path = wheelhouse_dir / whl_file
            print(f"Processing {wheel_path}")
            wheel_name = wheel_path.stem
            wheel_ext = wheel_path.suffix
            wheel_name_parts = wheel_name.split('-')
            package_name = wheel_name_parts[0]
            is_binary = 'cengal_light' == package_name
            package_version = wheel_name_parts[1]
            target_python_version = wheel_name_parts[2]
            is_cpython = wheel_name_parts[2].startswith('cp')
            if is_cpython:
                python_interpreter = 'CPython'
            else:
                python_interpreter = 'PyPy'
            
            python_version_str_raw = wheel_name_parts[2][2:]  # '38' for '3.8' version or '310' for '3.10' version
            python_version_str_prefix = '' if is_cpython else 'pypy-'
            python_version_str = python_version_str_prefix + '.'.join([python_version_str_raw[0], python_version_str_raw[1:]])
            target_abi = wheel_name_parts[3]
            target_os_and_arghitecture = wheel_name_parts[4]  # 'macosx_14_0_arm64' or 'macosx_13_0_x86_64'
            if target_os_and_arghitecture.endswith('x86_64'):
                target_architecture = 'x86_64'
                target_os = target_os_and_arghitecture[:-(1 + len(target_architecture))]
            elif target_os_and_arghitecture.endswith('amd64'):
                target_architecture = 'amd64'
                target_os = target_os_and_arghitecture[:-(1 + len(target_architecture))]
            elif target_os_and_arghitecture.endswith('arm64'):
                target_architecture = 'arm64'
                target_os = target_os_and_arghitecture[:-(1 + len(target_architecture))]
            else:
                print(f"Wheel {wheel_path} ignored because it has unknown architecture: {target_os_and_arghitecture}", file=sys.stderr)
                target_architecture = str()
                target_os = target_os_and_arghitecture
            
            update_wheel(package_name, target_python_version, python_interpreter, python_version_str, target_abi, target_os, target_architecture, target_os_and_arghitecture, wheel_path)
    finally:
        os.chdir(curdir)


def main():
    update_wheels()


if __name__ == '__main__':
    main()
