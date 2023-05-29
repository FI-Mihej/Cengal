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
__version__ = "3.2.5"
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

import argparse
import json
import os
import subprocess
import sys
import tempfile




__author__ = 'ButenkoMS <gtalk@butenkoms.space>'


VMBENCH_MASTER_ROOT_PATH = os.path.join('installed', 'vmbench-master')
HTTP_CLIENT_SCRIPT_NAME = 'http_client'
HTTP_CLIENT_FULL_PATH = os.path.join(os.path.expanduser("~"), VMBENCH_MASTER_ROOT_PATH, HTTP_CLIENT_SCRIPT_NAME)
RESULTS_OUTPUT_DIR = os.path.join(os.path.expanduser("~"), 'PycharmProjects', 'LocalExperiments',
                                  'ServerPerformanceTestsResults')


# luascript = """
# function done(summary, latency, requests)
#     tpl = [[
# {
#     "messages": %d,
#     "transfer": %.2f,
#     "rps": %.2f,
#     "latency_min": %.3f,
#     "latency_mean": %.3f,
#     "latency_max": %.3f,
#     "latency_std": %.3f,
#     "latency_cv": %.2f,
#     "latency_percentiles": [%s]
# }]]
#
#     transfer = (summary.bytes / (1024 * 1024)) / (summary.duration / 1000000)
#     rps = summary.requests / (summary.duration / 1000000)
#     latency_percentiles = {}
#     percentiles = {25, 50, 75, 90, 99, 99.99}
#
#     for i, percentile in ipairs(percentiles) do
#         table.insert(
#             latency_percentiles,
#             string.format("[%.2f, %.3f]", percentile,
#                           latency:percentile(percentile) / 1000)
#         )
#     end
#
#     out = string.format(tpl, summary.requests,  transfer, rps,
#                         latency.min / 1000, latency.mean / 1000,
#                         latency.max / 1000, latency.stdev / 1000,
#                         (latency.stdev / latency.mean) * 100,
#                         table.concat(latency_percentiles, ','))
#
#     io.stderr:write(out)
# end
# """
#
#
# def run_single_test(msize=1000, duration=30, concurrency=3, addr='127.0.0.1:18495', output_format='text'):
#     # parser = argparse.ArgumentParser()
#     # parser.add_argument('--msize', default=1000, type=int,
#     #                     help='message size in bytes')
#     # parser.add_argument('--duration', '-T', default=30, type=int,
#     #                     help='duration of test in seconds')
#     # parser.add_argument('--concurrency', default=3, type=int,
#     #                     help='request concurrency')
#     # parser.add_argument('--addr', default='127.0.0.1:18495', type=str,
#     #                     help='server address')
#     # parser.add_argument('--output-format', default='text', type=str,
#     #                     help='output format', choices=['text', 'json'])
#     # args = parser.parse_args()
#
#     unix = False
#     if args.addr.startswith('file:'):
#         abort('Unix sockets are not supported')
#
#     with tempfile.NamedTemporaryFile(mode='w+t', delete=False) as luaf:
#         luaf.write(luascript)
#         lua_script_path = luaf.name
#
#     wrk = ['/home/fi_mihej/installed/wrk/wrk', '--latency', '--duration={}s'.format(args.duration),
#            '--connections={}'.format(args.concurrency),
#            '--script={}'.format(lua_script_path),
#            'http://{}/{}'.format(args.addr, args.msize)]
#
#     try:
#         wrk_run = subprocess.Popen(wrk, universal_newlines=True,
#                                    stdout=subprocess.PIPE,
#                                    stderr=subprocess.PIPE)
#         out, data_json = wrk_run.communicate()
#     finally:
#         os.unlink(lua_script_path)
#
#     if args.output_format == 'json':
#         print(data_json)
#     else:
#         data = json.loads(data_json)
#
#         data['latency_percentiles'] = '; '.join(
#             '{}% under {}ms'.format(*v) for v in data['latency_percentiles'])
#
#         output = """\
# {messages} {size}KiB messages in {duration} seconds
# Latency: min {latency_min}ms; max {latency_max}ms; mean {latency_mean}ms; \
# std: {latency_std}ms ({latency_cv}%)
# Latency distribution: {latency_percentiles}
# Requests/sec: {rps}
# Transfer/sec: {transfer}MiB
# """.format(duration=args.duration, size=round(args.msize / 1024, 2), **data)
#
#         print(output)

def make_file_name_from_test_name(test_name: str) -> str:
    good_characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._-'
    result_string = ''
    for character in test_name:
        if character in good_characters:
            result_string += character
        else:
            result_string += ' '
    return result_string + '.json'


def main():
    test_name = ''
    if len(sys.argv) > 1:
        test_name = sys.argv[1]

    print()
    print('\t<<TEST STARTED: "{}">>:'.format(test_name))
    print()

    set_of_tests = list()

    #====
    # Разогрев 60 секунд. Не понятно почему, но он таки требуется (после него на Python 3.5.1 работа идет на
    # 30-50% быстрее)

    msizes = [1024**2, 10*1024, 1024, 100]
    concurrencies = [1, 200, 1000]
    duration = 5

    another_tests_set = ('warming-up', msizes, concurrencies, duration)
    set_of_tests.append(another_tests_set)

    #====
    # Тест количества соединений (при каком количестве соединений производительность наибольшая)

    msizes = [1024**2, 10*1024, 1024, 100]
    concurrencies = [1, 2, 10, 50, 100, 200, 500, 1000]
    duration = 2

    another_tests_set = ('concurency', msizes, concurrencies, duration)
    set_of_tests.append(another_tests_set)

    #====
    # Тест производительности от размера сообщения при наиболее производительном кол-ве соединений

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

    duration = 2

    another_tests_set = ('warming-up for a different message sizes cache', msizes, concurrencies, duration)
    set_of_tests.insert(1, another_tests_set)
    another_tests_set = ('message size', msizes, concurrencies, duration)
    set_of_tests.append(another_tests_set)

    #====

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
                # print('Testing msize {}'.format(msize))
                for concurrency in concurrencies:
                    another_test_run_parameters = '--msize={msize} --concurrency={concurrency} --duration={duration} ' \
                                                  '--addr="{host}:{port}" --output-format={output_format}'
                    another_test_run_parameters = another_test_run_parameters.format(
                        msize=msize, concurrency=concurrency, duration=duration, host='127.0.0.1', port=18495,
                        output_format='json')
                    # print(another_test_run_parameters)
                    another_test_run_parameters = 'python3 {path} {params}'.format(
                        path=HTTP_CLIENT_FULL_PATH, params=another_test_run_parameters)

                    run_parameters = shlex.split(another_test_run_parameters)
                    # print(run_parameters)

                    # call_result = subprocess.call(run_parameters)

                    test_run = subprocess.Popen(run_parameters, universal_newlines=True,
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                    data_json, test_run_err = test_run.communicate()

                    # print(data_json, test_run_err)
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


if __name__ == "__main__":
    main()
