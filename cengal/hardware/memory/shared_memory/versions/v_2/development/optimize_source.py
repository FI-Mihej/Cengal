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


__all__ = []


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""


__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.text_processing.open_text_file import OpenTextFile, TextFileInfo
from cengal.text_processing.text_processing import normalize_line_separators_and_tabs, replace_text, replace_slice, replace_dev_word
# from cengal.text_processing.help_tools import find_substring_full_word
from cengal.text_processing.brackets_processing import *
from cengal.file_system.path_manager import path_relative_to_src
from cengal.performance_test_lib import measure_time_tl
# from cengal.code_inspection.auto_line_tracer import ftr as tr
from cengal.code_inspection.auto_line_tracer import tr

from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional, Set


text_replacements = [
    # # ('', ''),
]


source_files: Dict[str, str] = {
    path_relative_to_src('../shared_memory.py'): path_relative_to_src('../generated_optimized_shared_memory.py'),
    path_relative_to_src('../../../../shared_memory_external_types/numpy_types/versions/v_0/numpy_types.py'): path_relative_to_src('../../../../shared_memory_external_types/numpy_types/versions/v_0/generated_optimized_numpy_types.py'),
    path_relative_to_src('../../../../shared_memory_external_types/torch_types/versions/v_0/torch_types.py'): path_relative_to_src('../../../../shared_memory_external_types/torch_types/versions/v_0/generated_optimized_torch_types.py'),
}


@dataclass
class ParsedEnum:
    name: str
    fields: List[Tuple[str, str, int]]


bs: int = 8


def dprint(data, data_slice: slice):
    if data_slice is None:
        return
    
    print('=' * 80)
    print('Data: \n', data[data_slice])
    new_start = data_slice.start - 10
    if new_start < 0:
        new_start = 0
    
    new_end = data_slice.stop + 10
    if new_end > len(data):
        new_end = len(data)
    
    adjusted_data_slice = slice(new_start, new_end)
    print('Adjusted Data: \n', data[adjusted_data_slice])
    print('=' * 80)
    print()


comment_slice: BracketPair = BracketPair([Bracket('#')], line_break_r_accessible_bounds)


def find_enum_header(content: str, enum_header_bracket_pair: BracketPair, start: int, stop: Optional[int] = None) -> Tuple[Optional[slice], Optional[slice]]:
    content_len: int = len(content)
    next_enum_header_slice: slice = None
    while next_enum_header_slice is None:
        another_line_slice: slice = find_text_with_brackets(content, line, start, stop)
        # dprint(content, another_line_slice)
        if another_line_slice is None:
            break

        temp_next_enum_header_slice: slice = find_text_with_brackets(content, enum_header_bracket_pair, another_line_slice.start, another_line_slice.stop)
        if temp_next_enum_header_slice is not None:
            another_line_slice_comment: slice = find_text_with_brackets(content, comment_slice, another_line_slice.start, another_line_slice.stop)
            if another_line_slice_comment is not None:
                print('Comment 0: ', content[another_line_slice_comment])
                code_within_another_line_slice = slice(another_line_slice.start, another_line_slice_comment.start)
            else:
                code_within_another_line_slice = another_line_slice
            
            next_enum_header_slice: slice = find_text_with_brackets(content, enum_header_bracket_pair, code_within_another_line_slice.start, code_within_another_line_slice.stop)
            if next_enum_header_slice is not None:
                another_line_slice: slice = find_text_with_brackets(content, line, start, stop)
                another_line_slice_comment: slice = find_text_with_brackets(content, comment_slice, another_line_slice.start, another_line_slice.stop)
                if another_line_slice_comment is not None:
                    print('Comment 1: ', content[another_line_slice_comment])
                    code_within_another_line_slice = slice(another_line_slice.start, another_line_slice_comment.start)
                else:
                    code_within_another_line_slice = another_line_slice
                
                next_enum_header_slice: slice = find_text_with_brackets(content, enum_header_bracket_pair, code_within_another_line_slice.start, code_within_another_line_slice.stop)

        start = another_line_slice.stop
        # dprint(content, next_enum_header_slice)
        if start >= content_len:
            break
    
    return another_line_slice, next_enum_header_slice


def enums_to_text_replacements():
    parsed_enums: List[ParsedEnum] = list()
    for src_file, _ in source_files.items():
        with OpenTextFile(src_file, 'rb') as source_text_file_info:
            source_text_file_info.text.existence = False
            content: str = source_text_file_info.text.value
            enum_header_bracket_pair: BracketPair = BracketPair([Bracket('class ')], [Bracket('(IntEnum):')])
            enum_field_name_bracket_pair: BracketPair = BracketPair(line_break_l_accessible_bounds, [Bracket('=')])
            enum_field_value_bracket_pair: BracketPair = BracketPair([Bracket('=')], line_break_r_accessible_bounds)

            next_enum_header_line_slice, next_enum_header_slice = find_enum_header(content, enum_header_bracket_pair, 0)
            while next_enum_header_slice is not None:
                enum_header_line_slice: slice = next_enum_header_line_slice
                enum_header_slice: slice = next_enum_header_slice
                if enum_header_slice is None:
                    break
                
                enum_start: int = enum_header_line_slice.stop
                next_enum_header_line_slice, next_enum_header_slice = find_enum_header(content, enum_header_bracket_pair, enum_start)
                if next_enum_header_slice is None:
                    enum_stop = None
                else:
                    enum_stop = next_enum_header_line_slice.start
                
                enum_class_name_slice: slice = find_text_in_brackets(content, enum_header_bracket_pair, enum_header_slice.start, enum_header_slice.stop)
                enum_class_name: str = content[enum_class_name_slice]

                enum_fields: List[Tuple[str, str, int]] = list()
                while True:
                    enum_field_line_slice: slice = find_text_with_brackets(content, line, enum_start, enum_stop)
                    if enum_field_line_slice is None:
                        break
                    
                    another_line_slice_comment: slice = find_text_with_brackets(content, comment_slice, enum_field_line_slice.start, enum_field_line_slice.stop)
                    if another_line_slice_comment is not None:
                        print('Comment 2: ', content[another_line_slice_comment])
                        code_within_enum_field_line_slice = slice(enum_field_line_slice.start, another_line_slice_comment.start)
                    else:
                        code_within_enum_field_line_slice = enum_field_line_slice
                    
                    enum_start = enum_field_line_slice.stop
                    # dprint(content, enum_field_line_slice)
                    enum_field_name_slice: slice = find_text_in_brackets(content, enum_field_name_bracket_pair, code_within_enum_field_line_slice.start, code_within_enum_field_line_slice.stop)
                    if enum_field_name_slice is None:
                        break
                    
                    enum_field_value_slice: slice = find_text_in_brackets(content, enum_field_value_bracket_pair, code_within_enum_field_line_slice.start, code_within_enum_field_line_slice.stop)
                    if enum_field_value_slice is None:
                        break
                    
                    enum_field_name: str = content[enum_field_name_slice].strip()
                    if not enum_field_name:
                        break

                    enum_field_str_value: str = content[enum_field_value_slice].strip()
                    if not enum_field_str_value:
                        break

                    try:
                        enum_field_value = int(enum_field_str_value)
                    except ValueError:
                        break

                    enum_fields.append((enum_field_name, enum_field_str_value, enum_field_value))
                
                enum_fields_sorted_by_name_len: List[Tuple[str, str, int]] = sorted(enum_fields, key=lambda enum_field: len(enum_field[0]), reverse=True)
                parsed_enums.append(ParsedEnum(enum_class_name, enum_fields_sorted_by_name_len))

    parsed_enums_sorted_by_enum_class_name_size: List[ParsedEnum] = sorted(parsed_enums, key=lambda parsed_enum: len(parsed_enum.name), reverse=True)
    tr(parsed_enums_sorted_by_enum_class_name_size)
    for parsed_enum in parsed_enums_sorted_by_enum_class_name_size:
        enum_class_name: str = parsed_enum.name
        enum_fields: List[Tuple[str, str, int]] = parsed_enum.fields
        enum_len: int = len(enum_fields)
        enum_len_str = str(enum_len)
        enum_len_bs: int = len(enum_fields) * bs
        enum_len_bs_str = str(enum_len_bs)
        text_replacements.append((f'bs * len({enum_class_name})', enum_len_bs_str))
        text_replacements.append((f'len({enum_class_name})', enum_len_str))
        for enum_field in enum_fields:
            enum_field_name, enum_field_str_value, enum_field_value = enum_field
            enum_field_value_bs: int = enum_field_value * bs
            enum_field_value_bs_str = str(enum_field_value_bs)
            text_replacements.append((f'bs * {enum_class_name}.{enum_field_name}.value', enum_field_value_bs_str))
            text_replacements.append((f'bs * {enum_class_name}.{enum_field_name}', enum_field_value_bs_str))
            text_replacements.append((f'{enum_class_name}.{enum_field_name}.value', enum_field_str_value))


text_words_replacements = [
    ('bs = block_size', '_bs = block_size'),
    ('bs', '8'),
    ('_bs = block_size', 'bs = block_size'),
]


def main():
    enums_to_text_replacements()
    tr(text_replacements)
    for source_file_path, result_file_path in source_files.items():
        with OpenTextFile(source_file_path, 'rb') as source_text_file_info:
            source_text_file_info.text.existence = False
            content: str = source_text_file_info.text.value
            for text_replacement_pair in text_replacements:
                before, after = text_replacement_pair
                content = replace_text(content, before, after)
            
            # if text_words_replacements:
            #     content = content.encode('utf-8')
            #     for text_replacement_pair in text_words_replacements:
            #         before, after = text_replacement_pair
            #         before = before.encode('utf-8')
            #         after = after.encode('utf-8')
            #         offset = 0
            #         start_index, end_index = -1, -1
            #         start_index, end_index = find_substring_full_word(content, before, offset, True)
            #         while (start_index is not None) and (end_index is not None):
            #             content, _ = replace_slice(content, slice(start_index, end_index), after)
            #             start_index, end_index = find_substring_full_word(content, before, offset, True)
                
            #     content = content.decode('utf-8')
            
            if text_words_replacements:
                for text_replacement_pair in text_words_replacements:
                    before, after = text_replacement_pair
                    content = replace_dev_word(content, before, after)

            with OpenTextFile(result_file_path, 'wb', encoding=source_text_file_info.encoding) as result_text_file_info:
                result_text_file_info.text.value = content


if '__main__' == __name__:
    main()
