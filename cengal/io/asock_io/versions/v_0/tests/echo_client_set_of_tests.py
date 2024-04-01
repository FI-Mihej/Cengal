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
__version__ = "4.3.2"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import os.path
import subprocess
import time
import shutil
import sys
import shlex




__author__ = 'ButenkoMS <gtalk@butenkoms.space>'


VMBENCH_MASTER_ROOT_PATH = os.path.join('installed', 'vmbench-master')
ECHO_CLIENT_SCRIPT_NAME = 'echo_client'
ECHO_CLIENT_FULL_PATH = os.path.join(os.path.expanduser("~"), VMBENCH_MASTER_ROOT_PATH, ECHO_CLIENT_SCRIPT_NAME)


def main():
    test_name = ''
    if len(sys.argv) > 1:
        test_name = sys.argv[1]

    print()
    print('\t<<TEST STARTED: "{}">>:'.format(test_name))
    print()
    multipliers = [
        [8 * 1000, 7 * 1000, 6 * 1000, 5 * 1000, 4 * 1000, 3 * 1000, 2 * 1000, 1000, 500, 200, 100, 50, 25, 20, 10, 5],
        [8 * 1024, 7 * 1024, 6 * 1024, 5 * 1024, 4 * 1024, 3 * 1024, 2 * 1024, 1024, 512, 256, 128, 64, 32, 16, 8, 4,
         2, 1]
    ]
    second_multipliers = [1460, 1024, 1]
    msizes_set = set()
    for second_multiplier in second_multipliers:
        for multiplier_list in multipliers:
            for multiplier in multiplier_list:
                msizes_set.add(multiplier * second_multiplier)
    msizes = sorted(list(msizes_set), reverse=True)

    concurrencies = [1, 2, 10, 50, 100, 200, 500, 1000]

    for msize in msizes:
        for concurrency in concurrencies:
            another_test_run_parameters = '--msize={msize} --mpr={mpr} --concurrency={concurrency} ' \
                                          '--duration={duration} --timeout={timeout} --addr="{host}:{port}"'
            another_test_run_parameters = another_test_run_parameters.format(
                msize=msize, mpr=1, concurrency=concurrency, duration=5, timeout=2, host='127.0.0.1', port=18495)
            print(another_test_run_parameters)
            another_test_run_parameters = 'python3 {path} {params}'.format(
                path=ECHO_CLIENT_FULL_PATH, params=another_test_run_parameters)

            call_result = subprocess.call(shlex.split(another_test_run_parameters))

    print('\t<<TEST FINISHED>>')
    print()
    print()


if __name__ == "__main__":
    main()
