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
__version__ = "4.4.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.text_processing.open_text_file import OpenTextFile, TextFileInfo
from cengal.text_processing.text_processing import normalize_line_separators_and_tabs, replace_text, replace_slice
from cengal.text_processing.help_tools import find_substring_full_word
from cengal.text_processing.brackets_processing import *
from cengal.file_system.path_manager import path_relative_to_src


text_replacements = [
    # ('bs * len(BaseObjOffsets)', '16'),
    # ('len(BaseObjOffsets)', '2'),
    # ('bs * BaseObjOffsets.obj_type', '0'),
    # ('bs * BaseObjOffsets.obj_size', '8'),
    
    ('bs * len(BaseObjOffsets)', '16'),
    ('len(BaseObjOffsets)', '2'),
    ('bs * BaseObjOffsets.obj_type.value', '0'),
    ('bs * BaseObjOffsets.obj_type', '0'),
    ('BaseObjOffsets.obj_type.value', '0'),
    ('bs * BaseObjOffsets.obj_size.value', '8'),
    ('bs * BaseObjOffsets.obj_size', '8'),
    ('BaseObjOffsets.obj_size.value', '1'),

    # ('bs * len(IntOffsets)', '8'),
    # ('len(IntOffsets)', '1'),
    # ('bs * IntOffsets.data', '0'),
    
    ('bs * len(IntOffsets)', '8'),
    ('len(IntOffsets)', '1'),
    ('bs * IntOffsets.data.value', '0'),
    ('bs * IntOffsets.data', '0'),
    ('IntOffsets.data.value', '0'),
    
    # ('bs * len(SmallIntOffsets)', '8'),
    # ('len(SmallIntOffsets)', '1'),
    # ('bs * SmallIntOffsets.data', '0'),
    
    ('bs * len(SmallIntOffsets)', '8'),
    ('len(SmallIntOffsets)', '1'),
    ('bs * SmallIntOffsets.data.value', '0'),
    ('bs * SmallIntOffsets.data', '0'),
    ('SmallIntOffsets.data.value', '0'),
    
    # ('bs * len(BigIntOffsets)', '16'),
    # ('len(BigIntOffsets)', '2'),
    # ('bs * BigIntOffsets.data_size', '0'),
    # ('bs * BigIntOffsets.data', '8'),
    
    ('bs * len(BigIntOffsets)', '16'),
    ('len(BigIntOffsets)', '2'),
    ('bs * BigIntOffsets.data_size.value', '0'),
    ('bs * BigIntOffsets.data_size', '0'),
    ('BigIntOffsets.data_size.value', '0'),
    ('bs * BigIntOffsets.data.value', '8'),
    ('bs * BigIntOffsets.data', '8'),
    ('BigIntOffsets.data.value', '1'),
    
    # ('bs * len(BoolOffsets)', '8'),
    # ('len(BoolOffsets)', '1'),
    # ('bs * BoolOffsets.data', '0'),
    
    ('bs * len(BoolOffsets)', '8'),
    ('len(BoolOffsets)', '1'),
    ('bs * BoolOffsets.data.value', '0'),
    ('bs * BoolOffsets.data', '0'),
    ('BoolOffsets.data.value', '0'),
    
    # ('bs * len(FloatOffsets)', '8'),
    # ('len(FloatOffsets)', '1'),
    # ('bs * FloatOffsets.data', '0'),
    
    ('bs * len(FloatOffsets)', '8'),
    ('len(FloatOffsets)', '1'),
    ('bs * FloatOffsets.data.value', '0'),
    ('bs * FloatOffsets.data', '0'),
    ('FloatOffsets.data.value', '0'),
    
    # ('bs * len(BytesOffsets)', '16'),
    # ('len(BytesOffsets)', '2'),
    # ('bs * BytesOffsets.data_size', '0'),
    # ('bs * BytesOffsets.data', '8'),
    
    ('bs * len(BytesOffsets)', '16'),
    ('len(BytesOffsets)', '2'),
    ('bs * BytesOffsets.data_size.value', '0'),
    ('bs * BytesOffsets.data_size', '0'),
    ('BytesOffsets.data_size.value', '0'),
    ('bs * BytesOffsets.data.value', '8'),
    ('bs * BytesOffsets.data', '8'),
    ('BytesOffsets.data.value', '1'),
    
    # ('bs * len(BytearrayOffsets)', '16'),
    # ('len(BytearrayOffsets)', '2'),
    # ('bs * BytearrayOffsets.data_size', '0'),
    # ('bs * BytearrayOffsets.data', '0'),
    
    ('bs * len(BytearrayOffsets)', '16'),
    ('len(BytearrayOffsets)', '2'),
    ('bs * BytearrayOffsets.data_size.value', '0'),
    ('bs * BytearrayOffsets.data_size', '0'),
    ('BytearrayOffsets.data_size.value', '0'),
    ('bs * BytearrayOffsets.data.value', '8'),
    ('bs * BytearrayOffsets.data', '8'),
    ('BytearrayOffsets.data.value', '1'),
    
    # ('bs * len(StrOffsets)', '16'),
    # ('len(StrOffsets)', '2'),
    # ('bs * StrOffsets.data_size', '0'),
    # ('bs * StrOffsets.data', '8'),
    
    ('bs * len(StrOffsets)', '16'),
    ('len(StrOffsets)', '2'),
    ('bs * StrOffsets.data_size.value', '0'),
    ('bs * StrOffsets.data_size', '0'),
    ('StrOffsets.data_size.value', '0'),
    ('bs * StrOffsets.data.value', '8'),
    ('bs * StrOffsets.data', '8'),
    ('StrOffsets.data.value', '1'),
    
    # ('bs * len(InternalListOffsets)', '16'),
    # ('len(InternalListOffsets)', '2'),
    # ('bs * InternalListOffsets.capacity', '0'),
    # ('bs * InternalListOffsets.size', '8'),
    
    ('bs * len(InternalListOffsets)', '16'),
    ('len(InternalListOffsets)', '2'),
    ('bs * InternalListOffsets.capacity.value', '0'),
    ('bs * InternalListOffsets.capacity', '0'),
    ('InternalListOffsets.capacity.value', '0'),
    ('bs * InternalListOffsets.size.value', '8'),
    ('bs * InternalListOffsets.size', '8'),
    ('InternalListOffsets.size.value', '1'),
    
    # ('bs * len(InternalListFieldOffsets)', '16'),
    # ('len(InternalListFieldOffsets)', '2'),
    # ('bs * InternalListFieldOffsets.field_type', '0'),
    # ('bs * InternalListFieldOffsets.offset_or_data', '8'),
    
    ('bs * len(InternalListFieldOffsets)', '16'),
    ('len(InternalListFieldOffsets)', '2'),
    ('bs * InternalListFieldOffsets.field_type.value', '0'),
    ('bs * InternalListFieldOffsets.field_type', '0'),
    ('InternalListFieldOffsets.field_type.value', '0'),
    ('bs * InternalListFieldOffsets.offset_or_data.value', '8'),
    ('bs * InternalListFieldOffsets.offset_or_data', '8'),
    ('InternalListFieldOffsets.offset_or_data.value', '1'),
    
    ('bs * len(InternalListFieldTypes)', '40'),
    ('len(InternalListFieldTypes)', '5'),
    ('bs * InternalListFieldTypes.tnone.value', '0'),
    ('bs * InternalListFieldTypes.tnone', '0'),
    ('InternalListFieldTypes.tnone.value', '0'),
    ('bs * InternalListFieldTypes.tobj.value', '8'),
    ('bs * InternalListFieldTypes.tobj', '8'),
    ('InternalListFieldTypes.tobj.value', '1'),
    ('bs * InternalListFieldTypes.tint.value', '16'),
    ('bs * InternalListFieldTypes.tint', '16'),
    ('InternalListFieldTypes.tint.value', '2'),
    ('bs * InternalListFieldTypes.tfloat.value', '24'),
    ('bs * InternalListFieldTypes.tfloat', '24'),
    ('InternalListFieldTypes.tfloat.value', '3'),
    ('bs * InternalListFieldTypes.tbool.value', '32'),
    ('bs * InternalListFieldTypes.tbool', '32'),
    ('InternalListFieldTypes.tbool.value', '4'),
    
    # ('bs * len(ListOffsets)', '8'),
    # ('len(ListOffsets)', '1'),
    # ('bs * ListOffsets.internal_list_offset', '0'),
    
    ('bs * len(ListOffsets)', '8'),
    ('len(ListOffsets)', '1'),
    ('bs * ListOffsets.internal_list_offset.value', '0'),
    ('bs * ListOffsets.internal_list_offset', '0'),
    ('ListOffsets.internal_list_offset.value', '0'),
    
    # ('bs * len(TupleOffsets)', '8'),
    # ('len(TupleOffsets)', '1'),
    # ('bs * TupleOffsets.size', '0'),
    
    ('bs * len(TupleOffsets)', '8'),
    ('len(TupleOffsets)', '1'),
    ('bs * TupleOffsets.size.value', '0'),
    ('bs * TupleOffsets.size', '0'),
    ('TupleOffsets.size.value', '0'),
    
    # ('bs * len(TupleFieldOffsets)', '8'),
    # ('len(TupleFieldOffsets)', '1'),
    # ('bs * TupleFieldOffsets.item_offset', '0'),
    
    ('bs * len(TupleFieldOffsets)', '8'),
    ('len(TupleFieldOffsets)', '1'),
    ('bs * TupleFieldOffsets.item_offset.value', '0'),
    ('bs * TupleFieldOffsets.item_offset', '0'),
    ('TupleFieldOffsets.item_offset.value', '0'),
    
    ('bs * len(DatetimeOffsets)', '8'),
    ('len(DatetimeOffsets)', '1'),
    ('bs * DatetimeOffsets.data_bytes_offset.value', '0'),
    ('bs * DatetimeOffsets.data_bytes_offset', '0'),
    ('DatetimeOffsets.data_bytes_offset.value', '0'),
    
    ('bs * len(DecimalOffsets)', '8'),
    ('len(DecimalOffsets)', '1'),
    ('bs * DecimalOffsets.data_tuple_offset.value', '0'),
    ('bs * DecimalOffsets.data_tuple_offset', '0'),
    ('DecimalOffsets.data_tuple_offset.value', '0'),
    
    ('bs * len(SliceOffsets)', '8'),
    ('len(SliceOffsets)', '1'),
    ('bs * SliceOffsets.data_tuple_offset.value', '0'),
    ('bs * SliceOffsets.data_tuple_offset', '0'),
    ('SliceOffsets.data_tuple_offset.value', '0'),
    
    ('bs * len(ComplexOffsets)', '8'),
    ('len(ComplexOffsets)', '1'),
    ('bs * ComplexOffsets.data_tuple_offset.value', '0'),
    ('bs * ComplexOffsets.data_tuple_offset', '0'),
    ('ComplexOffsets.data_tuple_offset.value', '0'),
    
    ('bs * len(FastSetOffsets)', '8'),
    ('len(FastSetOffsets)', '1'),
    ('bs * FastSetOffsets.data_tuple_offset.value', '0'),
    ('bs * FastSetOffsets.data_tuple_offset', '0'),
    ('FastSetOffsets.data_tuple_offset.value', '0'),
    
    # ('bs * len(FastDictOffsets)', '8'),
    # ('len(FastDictOffsets)', '1'),
    # ('bs * FastDictOffsets.data_tuple_offset', '0'),
    
    ('bs * len(FastDictOffsets)', '8'),
    ('len(FastDictOffsets)', '1'),
    ('bs * FastDictOffsets.data_tuple_offset.value', '0'),
    ('bs * FastDictOffsets.data_tuple_offset', '0'),
    ('FastDictOffsets.data_tuple_offset.value', '0'),
    
    # ('bs * len(MessageOffsets)', '24'),
    # ('len(MessageOffsets)', '3'),
    # ('bs * MessageOffsets.previous_message_offset', '0'),
    # ('bs * MessageOffsets.next_message_offset', '8'),
    # ('bs * MessageOffsets.item_offset', '16'),

    ('bs * len(MessageOffsets)', '24'),
    ('len(MessageOffsets)', '3'),
    ('bs * MessageOffsets.previous_message_offset.value', '0'),
    ('bs * MessageOffsets.previous_message_offset', '0'),
    ('MessageOffsets.previous_message_offset.value', '0'),
    ('bs * MessageOffsets.next_message_offset.value', '8'),
    ('bs * MessageOffsets.next_message_offset', '8'),
    ('MessageOffsets.next_message_offset.value', '1'),
    ('bs * MessageOffsets.item_offset.value', '16'),
    ('bs * MessageOffsets.item_offset', '16'),
    ('MessageOffsets.item_offset.value', '2'),
    
    ('len(ObjectType)', '19'),
    ('ObjectType.tfree_memory.value', '0'),
    ('ObjectType.tmessage.value', '1'),
    ('ObjectType.tnone.value', '2'),
    ('ObjectType.tbool.value', '3'),
    ('ObjectType.tint.value', '4'),
    ('ObjectType.tfloat.value', '5'),
    ('ObjectType.tcomplex.value', '6'),
    ('ObjectType.tstr.value', '7'),
    ('ObjectType.tbytes.value', '8'),
    ('ObjectType.tbytearray.value', '9'),
    ('ObjectType.ttuple.value', '10'),
    ('ObjectType.tlist.value', '11'),
    ('ObjectType.tmutableset.value', '12'),
    ('ObjectType.tset.value', '13'),
    ('ObjectType.tmutablemapping.value', '14'),
    ('ObjectType.tmapping.value', '15'),
    ('ObjectType.tfastdict.value', '16'),
    ('ObjectType.tclass.value', '17'),
    ('ObjectType.tpickable.value', '18'),
    ('ObjectType.tinternal_list.value', '19'),
    ('ObjectType.tsmallint.value', '20'),
    ('ObjectType.tbigint.value', '21'),
    ('ObjectType.tgeneralobject.value', '22'),
    ('ObjectType.tnumpyndarray.value', '23'),
    ('ObjectType.ttorchtensor.value', '24'),
    ('ObjectType.tstaticobject.value', '25'),
    ('ObjectType.tfastset.value', '26'),
    ('ObjectType.tslice.value', '27'),
    ('ObjectType.tdecimal.value', '28'),
    ('ObjectType.tdatetime.value', '29'),
    ('ObjectType.tstaticobjectwithslots.value', '30'),

    # ('ObjectType.tfree_memory', '0'),
    # ('ObjectType.tmessage', '1'),
    # ('ObjectType.tnone', '2'),
    # ('ObjectType.tbool', '3'),
    # ('ObjectType.tinternal_list', '16'),
    # ('ObjectType.tint', '4'),
    # ('ObjectType.tfloat', '5'),
    # ('ObjectType.tcomplex', '6'),
    # ('ObjectType.tstr', '7'),
    # ('ObjectType.tbytes', '8'),
    # ('ObjectType.tbytearray', '9'),
    # ('ObjectType.ttuple', '10'),
    # ('ObjectType.tlist', '11'),
    # ('ObjectType.tfastdict', '12'),
    # ('ObjectType.tset', '13'),
    # ('ObjectType.tclass', '14'),
    # ('ObjectType.tpickable', '15'),
    # ('ObjectType.tsmallint', '17'),
    # ('ObjectType.tbigint', '18'),

    ('len(SysValuesOffsets)', '13'),
    ('bs * SysValuesOffsets.total_mem_size', '0'),
    ('bs * SysValuesOffsets.data_start_offset', '8'),
    ('bs * SysValuesOffsets.data_size', '16'),
    ('bs * SysValuesOffsets.data_end_offset', '24'),
    ('bs * SysValuesOffsets.free_memory_search_start', '32'),
    ('bs * SysValuesOffsets.first_message_offset', '40'),
    ('bs * SysValuesOffsets.last_message_offset', '48'),
    ('bs * SysValuesOffsets.creator_in_charge', '56'),
    ('bs * SysValuesOffsets.consumer_in_charge', '64'),
    ('bs * SysValuesOffsets.creator_wants_to_be_in_charge', '72'),
    ('bs * SysValuesOffsets.consumer_wants_to_be_in_charge', '80'),
    ('bs * SysValuesOffsets.creator_ready', '88'),
    ('bs * SysValuesOffsets.consumer_ready', '96'),
    
    # ('(bs,', '(8,'),
    # (' bs ', ' 8 '),
    # (' bs)', ' 8)'),
    # (' bs]', ' 8]'),
    # (' bs\r\n', ' 8\r\n'),
    # (' bs\n', ' 8\n'),
    # (' bs:', ' 8:'),

    ('len(InternalListFieldTypes)', '5'),
    ('InternalListFieldTypes.tnone.value', '0'),
    ('InternalListFieldTypes.tobj.value', '1'),
    ('InternalListFieldTypes.tint.value', '2'),
    ('InternalListFieldTypes.tfloat.value', '3'),
    ('InternalListFieldTypes.tbool.value', '4'),
    
    # MutableSet
    ('bs * len(MutableSetOffsets)', '32'),
    ('len(MutableSetOffsets)', '4'),
    ('bs * MutableSetOffsets.size.value', '0'),
    ('bs * MutableSetOffsets.size', '0'),
    ('MutableSetOffsets.size.value', '0'),
    ('bs * MutableSetOffsets.capacity.value', '8'),
    ('bs * MutableSetOffsets.capacity', '8'),
    ('MutableSetOffsets.capacity.value', '1'),
    ('bs * MutableSetOffsets.hashmap_offset.value', '16'),
    ('bs * MutableSetOffsets.hashmap_offset', '16'),
    ('MutableSetOffsets.hashmap_offset.value', '2'),
    ('bs * MutableSetOffsets.refresh_counter.value', '24'),
    ('bs * MutableSetOffsets.refresh_counter', '24'),
    ('MutableSetOffsets.refresh_counter.value', '3'),

    ('bs * len(MutableSetHashmapFieldTypes)', '24'),
    ('len(MutableSetHashmapFieldTypes)', '3'),
    ('bs * MutableSetHashmapFieldTypes.tnone.value', '0'),
    ('bs * MutableSetHashmapFieldTypes.tnone', '0'),
    ('MutableSetHashmapFieldTypes.tnone.value', '0'),
    ('bs * MutableSetHashmapFieldTypes.tobj.value', '8'),
    ('bs * MutableSetHashmapFieldTypes.tobj', '8'),
    ('MutableSetHashmapFieldTypes.tobj.value', '1'),
    ('bs * MutableSetHashmapFieldTypes.tbucket.value', '16'),
    ('bs * MutableSetHashmapFieldTypes.tbucket', '16'),
    ('MutableSetHashmapFieldTypes.tbucket.value', '2'),

    ('bs * len(MutableSetHashmapItemOffsets)', '24'),
    ('len(MutableSetHashmapItemOffsets)', '3'),
    ('bs * MutableSetHashmapItemOffsets.field_type.value', '0'),
    ('bs * MutableSetHashmapItemOffsets.field_type', '0'),
    ('MutableSetHashmapItemOffsets.field_type.value', '0'),
    ('bs * MutableSetHashmapItemOffsets.field_hash.value', '8'),
    ('bs * MutableSetHashmapItemOffsets.field_hash', '8'),
    ('MutableSetHashmapItemOffsets.field_hash.value', '1'),
    ('bs * MutableSetHashmapItemOffsets.obj_or_bucket.value', '16'),
    ('bs * MutableSetHashmapItemOffsets.obj_or_bucket', '16'),
    ('MutableSetHashmapItemOffsets.obj_or_bucket.value', '2'),

    ('bs * len(MutableSetBucketFieldTypes)', '16'),
    ('len(MutableSetBucketFieldTypes)', '2'),
    ('bs * MutableSetBucketFieldTypes.tnone.value', '0'),
    ('bs * MutableSetBucketFieldTypes.tnone', '0'),
    ('MutableSetBucketFieldTypes.tnone.value', '0'),
    ('bs * MutableSetBucketFieldTypes.tobj.value', '8'),
    ('bs * MutableSetBucketFieldTypes.tobj', '8'),
    ('MutableSetBucketFieldTypes.tobj.value', '1'),

    ('bs * len(MutableSetBucketOffsets)', '24'),
    ('len(MutableSetBucketOffsets)', '3'),
    ('bs * MutableSetBucketOffsets.field_type.value', '0'),
    ('bs * MutableSetBucketOffsets.field_type', '0'),
    ('MutableSetBucketOffsets.field_type.value', '0'),
    ('bs * MutableSetBucketOffsets.field_hash.value', '8'),
    ('bs * MutableSetBucketOffsets.field_hash', '8'),
    ('MutableSetBucketOffsets.field_hash.value', '1'),
    ('bs * MutableSetBucketOffsets.obj.value', '16'),
    ('bs * MutableSetBucketOffsets.obj', '16'),
    ('MutableSetBucketOffsets.obj.value', '2'),
    
    # Set
    ('bs * len(SetOffsets)', '24'),
    ('len(SetOffsets)', '3'),
    ('bs * SetOffsets.size.value', '0'),
    ('bs * SetOffsets.size', '0'),
    ('SetOffsets.size.value', '0'),
    ('bs * SetOffsets.capacity.value', '8'),
    ('bs * SetOffsets.capacity', '8'),
    ('SetOffsets.capacity.value', '1'),
    ('bs * SetOffsets.hashmap_offset.value', '16'),
    ('bs * SetOffsets.hashmap_offset', '16'),
    ('SetOffsets.hashmap_offset.value', '2'),

    ('bs * len(SetHashmapFieldTypes)', '24'),
    ('len(SetHashmapFieldTypes)', '3'),
    ('bs * SetHashmapFieldTypes.tnone.value', '0'),
    ('bs * SetHashmapFieldTypes.tnone', '0'),
    ('SetHashmapFieldTypes.tnone.value', '0'),
    ('bs * SetHashmapFieldTypes.tobj.value', '8'),
    ('bs * SetHashmapFieldTypes.tobj', '8'),
    ('SetHashmapFieldTypes.tobj.value', '1'),
    ('bs * SetHashmapFieldTypes.tbucket.value', '16'),
    ('bs * SetHashmapFieldTypes.tbucket', '16'),
    ('SetHashmapFieldTypes.tbucket.value', '2'),

    ('bs * len(SetHashmapItemOffsets)', '24'),
    ('len(SetHashmapItemOffsets)', '3'),
    ('bs * SetHashmapItemOffsets.field_type.value', '0'),
    ('bs * SetHashmapItemOffsets.field_type', '0'),
    ('SetHashmapItemOffsets.field_type.value', '0'),
    ('bs * SetHashmapItemOffsets.field_hash.value', '8'),
    ('bs * SetHashmapItemOffsets.field_hash', '8'),
    ('SetHashmapItemOffsets.field_hash.value', '1'),
    ('bs * SetHashmapItemOffsets.obj_or_bucket.value', '16'),
    ('bs * SetHashmapItemOffsets.obj_or_bucket', '16'),
    ('SetHashmapItemOffsets.obj_or_bucket.value', '2'),

    ('bs * len(SetBucketOffsets)', '16'),
    ('len(SetBucketOffsets)', '2'),
    ('bs * SetBucketOffsets.field_hash.value', '0'),
    ('bs * SetBucketOffsets.field_hash', '0'),
    ('SetBucketOffsets.field_hash.value', '0'),
    ('bs * SetBucketOffsets.obj.value', '8'),
    ('bs * SetBucketOffsets.obj', '8'),
    ('SetBucketOffsets.obj.value', '1'),
    
    # MutableMapping
    ('bs * len(MutableMappingOffsets)', '32'),
    ('len(MutableMappingOffsets)', '4'),
    ('bs * MutableMappingOffsets.size.value', '0'),
    ('bs * MutableMappingOffsets.size', '0'),
    ('MutableMappingOffsets.size.value', '0'),
    ('bs * MutableMappingOffsets.capacity.value', '8'),
    ('bs * MutableMappingOffsets.capacity', '8'),
    ('MutableMappingOffsets.capacity.value', '1'),
    ('bs * MutableMappingOffsets.hashmap_offset.value', '16'),
    ('bs * MutableMappingOffsets.hashmap_offset', '16'),
    ('MutableMappingOffsets.hashmap_offset.value', '2'),
    ('bs * MutableMappingOffsets.refresh_counter.value', '24'),
    ('bs * MutableMappingOffsets.refresh_counter', '24'),
    ('MutableMappingOffsets.refresh_counter.value', '3'),

    ('bs * len(MutableMappingHashmapFieldTypes)', '24'),
    ('len(MutableMappingHashmapFieldTypes)', '3'),
    ('bs * MutableMappingHashmapFieldTypes.tnone.value', '0'),
    ('bs * MutableMappingHashmapFieldTypes.tnone', '0'),
    ('MutableMappingHashmapFieldTypes.tnone.value', '0'),
    ('bs * MutableMappingHashmapFieldTypes.tobj.value', '8'),
    ('bs * MutableMappingHashmapFieldTypes.tobj', '8'),
    ('MutableMappingHashmapFieldTypes.tobj.value', '1'),
    ('bs * MutableMappingHashmapFieldTypes.tbucket.value', '16'),
    ('bs * MutableMappingHashmapFieldTypes.tbucket', '16'),
    ('MutableMappingHashmapFieldTypes.tbucket.value', '2'),

    ('bs * len(MutableMappingHashmapItemOffsets)', '32'),
    ('len(MutableMappingHashmapItemOffsets)', '4'),
    ('bs * MutableMappingHashmapItemOffsets.field_type.value', '0'),
    ('bs * MutableMappingHashmapItemOffsets.field_type', '0'),
    ('MutableMappingHashmapItemOffsets.field_type.value', '0'),
    ('bs * MutableMappingHashmapItemOffsets.field_hash.value', '8'),
    ('bs * MutableMappingHashmapItemOffsets.field_hash', '8'),
    ('MutableMappingHashmapItemOffsets.field_hash.value', '1'),
    ('bs * MutableMappingHashmapItemOffsets.key_or_bucket.value', '16'),
    ('bs * MutableMappingHashmapItemOffsets.key_or_bucket', '16'),
    ('MutableMappingHashmapItemOffsets.key_or_bucket.value', '2'),
    ('bs * MutableMappingHashmapItemOffsets.value_or_none.value', '24'),
    ('bs * MutableMappingHashmapItemOffsets.value_or_none', '24'),
    ('MutableMappingHashmapItemOffsets.value_or_none.value', '3'),

    ('bs * len(MutableMappingBucketFieldTypes)', '16'),
    ('len(MutableMappingBucketFieldTypes)', '2'),
    ('bs * MutableMappingBucketFieldTypes.tnone.value', '0'),
    ('bs * MutableMappingBucketFieldTypes.tnone', '0'),
    ('MutableMappingBucketFieldTypes.tnone.value', '0'),
    ('bs * MutableMappingBucketFieldTypes.tobj.value', '8'),
    ('bs * MutableMappingBucketFieldTypes.tobj', '8'),
    ('MutableMappingBucketFieldTypes.tobj.value', '1'),

    ('bs * len(MutableMappingBucketOffsets)', '32'),
    ('len(MutableMappingBucketOffsets)', '4'),
    ('bs * MutableMappingBucketOffsets.field_type.value', '0'),
    ('bs * MutableMappingBucketOffsets.field_type', '0'),
    ('MutableMappingBucketOffsets.field_type.value', '0'),
    ('bs * MutableMappingBucketOffsets.field_hash.value', '8'),
    ('bs * MutableMappingBucketOffsets.field_hash', '8'),
    ('MutableMappingBucketOffsets.field_hash.value', '1'),
    ('bs * MutableMappingBucketOffsets.key_obj.value', '16'),
    ('bs * MutableMappingBucketOffsets.key_obj', '16'),
    ('MutableMappingBucketOffsets.key_obj.value', '2'),
    ('bs * MutableMappingBucketOffsets.value_obj.value', '24'),
    ('bs * MutableMappingBucketOffsets.value_obj', '24'),
    ('MutableMappingBucketOffsets.value_obj.value', '3'),
    
    # Mapping
    ('bs * len(MappingOffsets)', '24'),
    ('len(MappingOffsets)', '3'),
    ('bs * MappingOffsets.size.value', '0'),
    ('bs * MappingOffsets.size', '0'),
    ('MappingOffsets.size.value', '0'),
    ('bs * MappingOffsets.capacity.value', '8'),
    ('bs * MappingOffsets.capacity', '8'),
    ('MappingOffsets.capacity.value', '1'),
    ('bs * MappingOffsets.hashmap_offset.value', '16'),
    ('bs * MappingOffsets.hashmap_offset', '16'),
    ('MappingOffsets.hashmap_offset.value', '2'),

    ('bs * len(MappingHashmapFieldTypes)', '24'),
    ('len(MappingHashmapFieldTypes)', '3'),
    ('bs * MappingHashmapFieldTypes.tnone.value', '0'),
    ('bs * MappingHashmapFieldTypes.tnone', '0'),
    ('MappingHashmapFieldTypes.tnone.value', '0'),
    ('bs * MappingHashmapFieldTypes.tobj.value', '8'),
    ('bs * MappingHashmapFieldTypes.tobj', '8'),
    ('MappingHashmapFieldTypes.tobj.value', '1'),
    ('bs * MappingHashmapFieldTypes.tbucket.value', '16'),
    ('bs * MappingHashmapFieldTypes.tbucket', '16'),
    ('MappingHashmapFieldTypes.tbucket.value', '2'),

    ('bs * len(MappingHashmapItemOffsets)', '32'),
    ('len(MappingHashmapItemOffsets)', '4'),
    ('bs * MappingHashmapItemOffsets.field_type.value', '0'),
    ('bs * MappingHashmapItemOffsets.field_type', '0'),
    ('MappingHashmapItemOffsets.field_type.value', '0'),
    ('bs * MappingHashmapItemOffsets.field_hash.value', '8'),
    ('bs * MappingHashmapItemOffsets.field_hash', '8'),
    ('MappingHashmapItemOffsets.field_hash.value', '1'),
    ('bs * MappingHashmapItemOffsets.key_or_bucket.value', '16'),
    ('bs * MappingHashmapItemOffsets.key_or_bucket', '16'),
    ('MappingHashmapItemOffsets.key_or_bucket.value', '2'),
    ('bs * MappingHashmapItemOffsets.value_or_none.value', '24'),
    ('bs * MappingHashmapItemOffsets.value_or_none', '24'),
    ('MappingHashmapItemOffsets.value_or_none.value', '3'),

    ('bs * len(MappingBucketOffsets)', '24'),
    ('len(MappingBucketOffsets)', '3'),
    ('bs * MappingBucketOffsets.field_hash.value', '0'),
    ('bs * MappingBucketOffsets.field_hash', '0'),
    ('MappingBucketOffsets.field_hash.value', '0'),
    ('bs * MappingBucketOffsets.key_obj.value', '8'),
    ('bs * MappingBucketOffsets.key_obj', '8'),
    ('MappingBucketOffsets.key_obj.value', '1'),
    ('bs * MappingBucketOffsets.value_obj.value', '16'),
    ('bs * MappingBucketOffsets.value_obj', '16'),
    ('MappingBucketOffsets.value_obj.value', '2'),

    # General Object
    ('bs * len(GeneralObjectOffsets)', '24'),
    ('len(GeneralObjectOffsets)', '3'),
    ('bs * GeneralObjectOffsets.pickled_obj.value', '0'),
    ('bs * GeneralObjectOffsets.pickled_obj', '0'),
    ('GeneralObjectOffsets.pickled_obj.value', '0'),
    ('bs * GeneralObjectOffsets.obj_dict.value', '8'),
    ('bs * GeneralObjectOffsets.obj_dict', '8'),
    ('GeneralObjectOffsets.obj_dict.value', '1'),
    ('bs * GeneralObjectOffsets.setable_data_descriptor_field_names.value', '16'),
    ('bs * GeneralObjectOffsets.setable_data_descriptor_field_names', '16'),
    ('GeneralObjectOffsets.setable_data_descriptor_field_names.value', '2'),

    # Static Object
    ('bs * len(StaticObjectOffsets)', '32'),
    ('len(StaticObjectOffsets)', '4'),
    ('bs * StaticObjectOffsets.pickled_obj.value', '0'),
    ('bs * StaticObjectOffsets.pickled_obj', '0'),
    ('StaticObjectOffsets.pickled_obj.value', '0'),
    ('bs * StaticObjectOffsets.pickled_attributes_dict.value', '8'),
    ('bs * StaticObjectOffsets.pickled_attributes_dict', '8'),
    ('StaticObjectOffsets.pickled_attributes_dict.value', '1'),
    ('bs * StaticObjectOffsets.attributes_slots.value', '16'),
    ('bs * StaticObjectOffsets.attributes_slots', '16'),
    ('StaticObjectOffsets.attributes_slots.value', '2'),
    ('bs * StaticObjectOffsets.setable_data_descriptor_field_names.value', '24'),
    ('bs * StaticObjectOffsets.setable_data_descriptor_field_names', '24'),
    ('StaticObjectOffsets.setable_data_descriptor_field_names.value', '3'),

    # Numpy ndarray
    ('bs * len(TNumpyNdarrayOffsets)', '24'),
    ('len(TNumpyNdarrayOffsets)', '3'),
    ('bs * TNumpyNdarrayOffsets.data_buffer_offset.value', '0'),
    ('bs * TNumpyNdarrayOffsets.data_buffer_offset', '0'),
    ('TNumpyNdarrayOffsets.data_buffer_offset.value', '0'),
    ('bs * TNumpyNdarrayOffsets.shape_tuple_offset.value', '8'),
    ('bs * TNumpyNdarrayOffsets.shape_tuple_offset', '8'),
    ('TNumpyNdarrayOffsets.shape_tuple_offset.value', '1'),
    ('bs * TNumpyNdarrayOffsets.pickled_datatype_offset.value', '16'),
    ('bs * TNumpyNdarrayOffsets.pickled_datatype_offset', '16'),
    ('TNumpyNdarrayOffsets.pickled_datatype_offset.value', '2'),
    
    # Numpy ndarray
    ('bs * len(TTorchTensorOffsets)', '8'),
    ('len(TTorchTensorOffsets)', '1'),
    ('bs * TTorchTensorOffsets.numpy_ndarray_offset.value', '0'),
    ('bs * TTorchTensorOffsets.numpy_ndarray_offset', '0'),
    ('TTorchTensorOffsets.numpy_ndarray_offset.value', '0'),

    # ('', ''),
]


text_words_replacements = [
    ('bs = block_size', '_bs = block_size'),
    ('bs', '8'),
    ('_bs = block_size', 'bs = block_size'),
]


def main():
    source_file_path: str = path_relative_to_src('../shared_memory.py')
    result_file_path: str = path_relative_to_src('../generated_optimized_shared_memory.py')
    with OpenTextFile(source_file_path, 'rb') as source_text_file_info:
        source_text_file_info.text.existence = False
        content: str = source_text_file_info.text.value
        for text_replacement_pair in text_replacements:
            before, after = text_replacement_pair
            content = replace_text(content, before, after)
        
        if text_words_replacements:
            content = content.encode('utf-8')
            for text_replacement_pair in text_words_replacements:
                before, after = text_replacement_pair
                before = before.encode('utf-8')
                after = after.encode('utf-8')
                offset = 0
                start_index, end_index = -1, -1
                start_index, end_index = find_substring_full_word(content, before, offset, True)
                while (start_index is not None) and (end_index is not None):
                    content, _ = replace_slice(content, slice(start_index, end_index), after)
                    start_index, end_index = find_substring_full_word(content, before, offset, True)
            
            content = content.decode('utf-8')

        with OpenTextFile(result_file_path, 'wb', encoding=source_text_file_info.encoding) as result_text_file_info:
            result_text_file_info.text.value = content


if '__main__' == __name__:
    main()
