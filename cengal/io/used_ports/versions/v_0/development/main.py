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
__version__ = "3.1.17"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


"""Extract all tables from an html file, printing and saving each to csv file.
https://stackoverflow.com/questions/2870667/how-to-convert-an-html-table-to-an-array-in-python
"""

import pandas as pd
import requests
from shutil import copyfile
import pickle
import csv

from cengal.file_system.path_manager import path_relative_to_src
from cengal.text_processing.brackets_processing import find_text_with_brackets, square
from cengal.text_processing.text_processing import replace_slice


def remove_square_brackets(text: str) -> str:
    br_slice = find_text_with_brackets(text, square)
    while br_slice is not None:
        text, _ = replace_slice(text, br_slice, str())
        br_slice = find_text_with_brackets(text, square)
    
    return text


html = requests.get('https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers').content
df_list = pd.read_html(html)
# df_list = pd.read_html('my_file.html')

for i, df in enumerate(df_list):
    res_table = list()
    print()
    print('============================')
    print(f'Table #{i}')
    df = df.replace({float('nan'): None})
    # print(df)
    print(tuple(df.columns))
    collumns_num = len(df.columns)
    for index, row in df.iterrows():
        res_row = list()
        for item_index, item in enumerate(row):
            item = item if item is None else remove_square_brackets(item)
            if 0 == item_index:
                # Port or ports range
                if item is not None:
                    port_range_delimiter = '–'
                    if port_range_delimiter in item:
                        item = tuple(item.split(port_range_delimiter))
            
            res_row.append(item)
        
        if index <= 10:
            row_tuple = tuple(res_row)
            print(row_tuple)
            if (i == 5) and (index == 1):
                nan_val = row_tuple[1]
                print(f'Val: {nan_val}; of type: {type(nan_val)}.')
            # print(row[0], row[1])
        
        res_table.append(res_row)
    
    table_name = None
    if 5 == i:
        table_name = 'system'
        known_ports = set(df['Port'])
        print(f'{table_name} has {len(known_ports)} known ports and ranges.')
    elif 6 == i:
        table_name = 'user'
        known_ports = set(df['Port'])
        print(f'{table_name} has {len(known_ports)} known ports and ranges.')
    elif 7 == i:
        table_name = 'ephemeral'
        known_ports = set(df['Port'])
        print(f'{table_name} has {len(known_ports)} known ports and ranges.')
    
    # df.to_csv(path_relative_to_src(f'data/table_{i}.csv'))
    # df.to_pickle(path_relative_to_src(f'data/table_{i}.pickle'))
    if table_name is not None:
        # df.to_csv(path_relative_to_src(f'data/table_{table_name}.csv'))
        # df.to_pickle(path_relative_to_src(f'data/table_{table_name}.pickle'))
        # copyfile(path_relative_to_src(f'data/table_{i}.pickle'), path_relative_to_src(f'data/table_{table_name}.pickle'))
        with open(path_relative_to_src(f'data/table_{table_name}.csv'), "w", newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(res_table)

        with open(path_relative_to_src(f'../data/table_{table_name}.pickle'), 'wb') as file:
            pickle.dump(res_table, file)
