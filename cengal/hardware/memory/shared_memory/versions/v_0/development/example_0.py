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
__version__ = "4.1.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import array
from multiprocessing import shared_memory

# Define the array type and length
arr_type = 'd'  # Example type (double)
arr_length = 10  # Example length

# Calculate the byte size of the array
arr_item_size = array.array(arr_type).itemsize
arr_byte_size = arr_length * arr_item_size

# Create a shared memory object
shm = shared_memory.SharedMemory(create=True, size=arr_byte_size)

# Create an array from the shared memory
arr = array.array(arr_type, shm.buf)

# Now you can use 'arr' as a regular array object
for i in range(arr_length):
    arr[i] = i * 1.0

# Print the shared memory buffer contents as a list of array.array elements
print("Shared memory buffer contents:", list(arr))

# When done, close and unlink the shared memory object
shm.close()
shm.unlink()
