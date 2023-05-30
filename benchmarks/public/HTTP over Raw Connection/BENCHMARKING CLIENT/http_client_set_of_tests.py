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
__version__ = "3.2.6"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import os.path
import shlex
import json
import os
import subprocess
import sys




__author__ = 'ButenkoMS <gtalk@butenkoms.space>'


HTTP_CLIENT_SCRIPT_NAME = 'http_client'
VMBENCH_MASTER_ROOT_PATH = os.path.normpath('your_local_tools/vmbench-master')  # relative to the user home directory
HTTP_CLIENT_FULL_PATH = os.path.join(os.path.expanduser("~"), VMBENCH_MASTER_ROOT_PATH, HTTP_CLIENT_SCRIPT_NAME)
RELATIVE_RESULTS_OUTPUT_DIR = os.path.normpath('YourPerformanceTestsResults/Servers')  # folder for test results (for
#   a json files with test results). Relative to the user home directory
RESULTS_OUTPUT_DIR = os.path.join(os.path.expanduser("~"), RELATIVE_RESULTS_OUTPUT_DIR)


def make_file_name_from_test_name(test_name: str) -> str:
    good_characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._-'
    result_string = ''
    for character in test_name:
        if character in good_characters:
            result_string += character
        else:
            result_string += ' '
    return result_string + '.json'


def add_test__1(set_of_tests):
    """
    Test #1: Preheat
    :param set_of_tests:
    :return:
    """

    msizes = [1024**2, 10*1024, 1024, 100]
    concurrencies = [1, 200, 1000]
    duration = 5  # each test duration == 5 seconds

    another_tests_set = ('Preheat', msizes, concurrencies, duration)
    set_of_tests.append(another_tests_set)


def add_test__3(set_of_tests):
    """
    Test # 3: Concurrency test (finds out at how many connections we have the best performance)
    :param set_of_tests:
    :return:
    """

    msizes = [1024**2, 10*1024, 1024, 100]
    concurrencies = [1, 2, 10, 50, 100, 200, 500, 1000]
    duration = 2  # each test duration == 2 seconds

    another_tests_set = ('Concurency', msizes, concurrencies, duration)
    set_of_tests.append(another_tests_set)


def add_tests__2_and_4(set_of_tests):
    """
    Tests #2 and #4.
    Test #2: heating up
    Test #4: message size test. Uses 200 concurrent connections (most performance in my case for all kind of servers
    (Python AsyncIO, GoLang, NodeJS, etc.). Test uses messages with size of [1 - 1460 * 1000 * 8] bytes. Where 1460 is
    an ordinary MSS (maximum segment size) for TCP under IPv4.
    :param set_of_tests:
    :return:
    """

    multipliers = [
        [1000, 500, 200, 100, 50, 25, 20, 10, 5, 4, 3, 2, 1],
        [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],
        [8 * 1000, 7 * 1000, 6 * 1000, 5 * 1000, 4 * 1000, 3 * 1000, 2 * 1000],
        [8 * 1024, 7 * 1024, 6 * 1024, 5 * 1024, 4 * 1024, 3 * 1024, 2 * 1024]
    ]
    second_multipliers = [1460, 1024, 1]
    msizes_set = set()
    for second_multiplier in second_multipliers:
        if 1024 == second_multiplier:
            for multiplier_list in multipliers:
                for multiplier in multiplier_list:
                    msizes_set.add(multiplier * second_multiplier)
        elif 1 == second_multiplier:
            for multiplier in multipliers[0] + multipliers[1]:
                msizes_set.add(multiplier * second_multiplier)
        elif 1460 == second_multiplier:
            for multiplier in multipliers[0][1:] + multipliers[2]:
                msizes_set.add(multiplier * second_multiplier)

    msizes = sorted(list(msizes_set), reverse=True)

    # concurrencies = [2, 10, 50, 100, 200, 500, 1000]
    concurrencies = [200]

    duration = 2  # each test duration == 2 seconds

    # Adding Test #2:
    another_tests_set = ('Warming-up for full list of a different message sizes', msizes, concurrencies, duration)
    set_of_tests.insert(1, another_tests_set)
    # Adding Test #4:
    another_tests_set = ('Full list of a different message sizes', msizes, concurrencies, duration)
    set_of_tests.append(another_tests_set)


def run_all_tests(set_of_tests, test_name):
    tests_set = list()

    for another_test_pack in set_of_tests:
        test_pack_name, msizes, concurrencies, duration = another_test_pack

        test_results = list()

        printable_full_result_text_template = 'Test pack name: "{name}"\n\tDuration of each test case: {duration}s...\n'
        single_result_text_template = '\tT {msize}B-{concurrency}C: {rps}R/s; {transfer}MiB/s.|'

        printable_full_result_text_title = printable_full_result_text_template.format(
            name=test_pack_name, duration=duration)
        print(printable_full_result_text_title)
        printable_full_result_text = ''

        try:
            for msize in msizes:
                for concurrency in concurrencies:
                    another_test_run_parameters = '--msize={msize} --concurrency={concurrency} --duration={duration} ' \
                                                  '--addr="{host}:{port}" --output-format={output_format}'
                    another_test_run_parameters = another_test_run_parameters.format(
                        msize=msize, concurrency=concurrency, duration=duration, host='127.0.0.1', port=18495,
                        output_format='json')
                    another_test_run_parameters = 'python3 {path} {params}'.format(
                        path=HTTP_CLIENT_FULL_PATH, params=another_test_run_parameters)

                    run_parameters = shlex.split(another_test_run_parameters)

                    test_run = subprocess.Popen(run_parameters, universal_newlines=True,
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                    data_json, test_run_err = test_run.communicate()

                    result_data = None
                    try:
                        result_data = json.loads(data_json)
                    except ValueError:
                        print('Test Script Out:', data_json, ';\nTest Script Err:', test_run_err)
                        raise
                    another_result = dict()
                    another_result['condition'] = {'msize': msize, 'concurrency': concurrency}
                    another_result['result_data'] = result_data
                    test_results.append(another_result)

                    single_result_text = single_result_text_template.format(
                        msize=msize, concurrency=concurrency, rps=result_data['rps'], transfer=result_data['transfer'])
                    printable_full_result_text += single_result_text
        except ValueError as err:
            print(err.args)

        print(printable_full_result_text)
        print()

        another_test_pack_dict = dict()
        another_test_pack_dict['test_pack_name'] = test_pack_name
        another_test_pack_dict['test_pack_data'] = test_results
        tests_set.append(another_test_pack_dict)

    full_test_result = dict()
    full_test_result['name'] = test_name
    full_test_result['tests_set'] = tests_set
    full_test_result_json = json.dumps(full_test_result)
    full_test_result_file_name = os.path.join(RESULTS_OUTPUT_DIR, make_file_name_from_test_name(test_name))
    with open(full_test_result_file_name, 'w') as file:
        file.write(full_test_result_json)

    print('\t<<TEST FINISHED>>')
    print()
    print()


def main():
    test_name = ''
    if len(sys.argv) > 1:
        test_name = sys.argv[1]

    print()
    print('\t<<TEST STARTED: "{}">>:'.format(test_name))
    print()

    set_of_tests = list()

    # ============
    # ADDING TESTS
    add_test__1(set_of_tests)
    add_test__3(set_of_tests)
    add_tests__2_and_4(set_of_tests)

    # =================
    # RUNNING ALL TESTS
    run_all_tests(set_of_tests, test_name)


if __name__ == "__main__":
    main()
