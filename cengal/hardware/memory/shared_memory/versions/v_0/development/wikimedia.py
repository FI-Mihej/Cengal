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
__version__ = "3.2.2"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


#!/usr/bin/env python



# from file_system import filtered_file_list_traversal, filtered_file_list, FilteringType, change_current_dir
import os
import sys
import mmap
from enum import Enum






PAGESIZE = mmap.PAGESIZE
IS_MSWINDOWS = (sys.platform == "win32")

# if not IS_MSWINDOWS:
#     from resource import getpagesize
# else:
#     def getpagesize():
#         return 0


MYSQLD_SOCKET = '/var/run/mysqld/mysqld.sock'
BAD_ENGINE_STRING = 'ENGINE=InnoDB'.encode()
GOOD_ENGINE_STRING = 'ENGINE=MyISAM'.encode()
if len(BAD_ENGINE_STRING) != len(GOOD_ENGINE_STRING):
    raise Exception('BAD_ENGINE_STRING and GOOD_ENGINE_STRING should have equal size!')
ENGINE_STRING_LEN = len(BAD_ENGINE_STRING)
ENDING_STRING_FOR_SQL_DUMPS = '\n\nCOMMIT; \nSET unique_checks=1; \nSET foreign_key_checks=1;\n'.encode()
INIT_COMMAND_FOR_MYSQL = 'SET autocommit=0; SET unique_checks=0; SET foreign_key_checks=0;'
MYSQL_RUN_COMMAND = 'mysql --batch --column-names --skip-comments --force --init-command="{init_command}" ' \
                    '--max_allowed_packet=512MB --net_buffer_length=280000 --password={password} --protocol=SOCKET ' \
                    '--reconnect --sigint-ignore --socket={socket} --ssl-mode=DISABLED -u {user_name} ' \
                    '--wait {db_name} < {sql_dump_name}'


class _FilteringType(Enum):
    including = 0  # include only files with extensions within the set of extensions
    excluding = 1  # filter out files with extensions within the set of extensions
    off = 2  # any file will fit criteria


def _filtered_file_list(root_dir, filtering_type, extentions_set=None):
    '''
    :param root_dir: str(); r'C:\dir\path'
    :param filtering_type: _FilteringType()
    :param extentions_set: set(); {'.upk', '.txt'}
    :return: tuple(); (dirpath, dirnames, new_filenames)
    '''

    if (_FilteringType.off != filtering_type) and (extentions_set is None):
        raise Exception('extentions_set can\'t be None with this filtering type')

    result = None
    raw_result = next(os.walk(root_dir))
    dirpath = raw_result[0]
    dirnames = raw_result[1]
    filenames = raw_result[2]

    new_filenames = list()
    for filename in filenames:
        if _FilteringType.off == filtering_type:
            new_filenames.append(filename)
        elif _FilteringType.including == filtering_type:
            extention = os.path.splitext(filename)[1]
            if extention in extentions_set:
                new_filenames.append(filename)
        elif _FilteringType.excluding == filtering_type:
            extention = os.path.splitext(filename)[1]
            if extention not in extentions_set:
                new_filenames.append(filename)

    result = (dirpath, dirnames, new_filenames)
    return result


def get_sql_file_names(root_dir):
    dirpath, dirnames, filenames = _filtered_file_list(root_dir, _FilteringType.including, {'.sql'})
    return filenames


def flush_mmap(mmap_obj, offset, size, file_name):
    # print('FLUSH: {}'.format(file_name))
    # print('closed: {}; size: {}; curr pos: {}; offset: {}; size: {}'.format(mmap_obj.closed, mmap_obj.size(), mmap_obj.tell(), offset, size))
    try:
        if IS_MSWINDOWS:
            if not mmap_obj.flush(offset, size):
                raise Exception('WIN32 EXCEPTION WITH: FILE: {}; ON FLUSH()'.format(file_name))
            else:
                print('FLUSHED...')
        else:
            # print('PAGE SIZE: {}'.format(PAGESIZE))
            n_x_pagesize = PAGESIZE * (offset // PAGESIZE)
            bytes_delta = offset - n_x_pagesize
            result_offset = n_x_pagesize
            result_size = size + bytes_delta
            if not mmap_obj.flush(result_offset, result_size):
                print('FLUSHED...')
    except:
        print()
        print('!EXCEPTION WITH: FILE: {}; ON FLUSH()'.format(file_name))
        print()
        # mmap_obj.close()
        raise


def find_in_mmap(mmap_obj, search_str, search_offset):
    file_len = mmap_obj.size()
    if (file_len - 1 - search_offset) >= len(search_str):
        return mmap_obj.find(search_str, search_offset)
    else:
        return -1


def replace_engine_string(mmap_obj, file_name):
    search_offset = 0
    bad_engine_string_start_pos = find_in_mmap(mmap_obj, BAD_ENGINE_STRING, search_offset)
    search_offset = bad_engine_string_start_pos
    while bad_engine_string_start_pos >= 0:
        mmap_obj[bad_engine_string_start_pos: bad_engine_string_start_pos + ENGINE_STRING_LEN] = GOOD_ENGINE_STRING
        # mmap_obj.seek(bad_engine_string_start_pos, os.SEEK_SET)
        # mmap_obj.write(GOOD_ENGINE_STRING)
        flush_mmap(mmap_obj, bad_engine_string_start_pos, ENGINE_STRING_LEN, file_name)
        bad_engine_string_start_pos = find_in_mmap(mmap_obj, BAD_ENGINE_STRING, search_offset)
        search_offset = bad_engine_string_start_pos


def append_ending_string(mmap_obj, file_name):
    current_file_len = mmap_obj.size()  # 2254
    # print('current_file_len: {}'.format(current_file_len))
    mmap_obj.resize(current_file_len + len(ENDING_STRING_FOR_SQL_DUMPS))  # 2254 + 58 = 2312
    # print('new_file_len: {}'.format(mmap_obj.size()))
    mmap_obj[current_file_len: current_file_len + len(ENDING_STRING_FOR_SQL_DUMPS)] = ENDING_STRING_FOR_SQL_DUMPS
    flush_mmap(mmap_obj, current_file_len, len(ENDING_STRING_FOR_SQL_DUMPS), file_name)


def modify_sql_dump(file_name):
    with open(file_name, 'r+b') as f:
        with mmap.mmap(f.fileno(), 0) as mm:
            replace_engine_string(mm, file_name)
            print('ENGINE WAS REPLACED...')
            append_ending_string(mm, file_name)
            print('ENDING STRING WAS APPEND...')


def run_mysql_import(file_name, db_name, user_name, password):
    result_command = MYSQL_RUN_COMMAND.format(db_name=db_name,
                                              user_name=user_name,
                                              password=password,
                                              sql_dump_name=file_name,
                                              socket=MYSQLD_SOCKET,
                                              init_command=INIT_COMMAND_FOR_MYSQL)
    os.system(result_command)


def main():
    print()
    mysql_user_name = input('Enter User Name: ')
    mysql_password = input('Enter Password: ')
    mysql_db_name = input('Enter DB Name: ')
    print()

    root_dir = os.getcwd()
    filenames = get_sql_file_names(root_dir)
    for sql_dump in filenames:
        print('START ON: {}:'.format(sql_dump))
        try:
            modify_sql_dump(sql_dump)
            print('DUMP MODIFY DONE...'.format(sql_dump))
            run_mysql_import(sql_dump, mysql_db_name, mysql_user_name, mysql_password)
            print('DUMP IMPORT DONE...'.format(sql_dump))
        except:
            print('!EXCEPTION ON DUMP {}!'.format(sql_dump))
            # raise
        print('END WITH: {}.'.format(sql_dump))
        print()


if __name__ == '__main__':
    main()
