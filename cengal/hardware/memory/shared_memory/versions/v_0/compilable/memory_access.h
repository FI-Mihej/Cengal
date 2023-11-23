// Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// 
//     http://www.apache.org/licenses/LICENSE-2.0
// 
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.


#ifndef MEMORY_ACCESS_H
#define MEMORY_ACCESS_H

void c_write_uint64(unsigned long long base_address, unsigned long long offset, unsigned long long value);
unsigned long long c_read_uint64(unsigned long long base_address, unsigned long long offset);
void c_write_int64(unsigned long long base_address, unsigned long long offset, long long value);
long long c_read_int64(unsigned long long base_address, unsigned long long offset);
void c_write_uint32(unsigned long long base_address, unsigned long long offset, unsigned int value);
unsigned int c_read_uint32(unsigned long long base_address, unsigned long long offset);
void c_write_int32(unsigned long long base_address, unsigned long long offset, int value);
int c_read_int32(unsigned long long base_address, unsigned long long offset);
void c_write_uint16(unsigned long long base_address, unsigned long long offset, unsigned short value);
unsigned short c_read_uint16(unsigned long long base_address, unsigned long long offset);
void c_write_int16(unsigned long long base_address, unsigned long long offset, short value);
short c_read_int16(unsigned long long base_address, unsigned long long offset);
void c_write_uint8(unsigned long long base_address, unsigned long long offset, unsigned char value);
unsigned char c_read_uint8(unsigned long long base_address, unsigned long long offset);
void c_write_int8(unsigned long long base_address, unsigned long long offset, char value);
char c_read_int8(unsigned long long base_address, unsigned long long offset);
void c_write_float(unsigned long long base_address, unsigned long long offset, float value);
float c_read_float(unsigned long long base_address, unsigned long long offset);
void c_write_double(unsigned long long base_address, unsigned long long offset, double value);
double c_read_double(unsigned long long base_address, unsigned long long offset);
void c_copy_memory(unsigned long long base_address, unsigned long long offset, unsigned long long size, unsigned long long source_offset);
void c_copy_memory_from(unsigned long long base_address, unsigned long long offset, unsigned long long size, unsigned long long source_offset);
void c_set_memory(unsigned long long base_address, unsigned long long offset, unsigned long long size, unsigned char value);
void c_zero_memory(unsigned long long base_address, unsigned long long offset, unsigned long long size);

#endif
