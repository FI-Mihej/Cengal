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


__all__ = [
]


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


from cengal.hardware.memory.shared_memory import *
from cengal.parallel_execution.asyncio.ashared_memory_manager import *


def sender():
    with SharedMemory('shared_objects', True, 1000 * 1024**2) as sm:
        some_data: bytes = bytes(400_000)
        sm.wait_consumer_ready()
        with wait_my_turn(sm):
            mapped_flag_holder = sm.put_message([False, False])

        msgs_to_send = 1000
        while msgs_to_send:
            with wait_my_turn(sm, periodic_sleep_time=None):
                if mapped_flag_holder[0]:
                    try:
                        while msgs_to_send:
                            sm.put_message(some_data)
                            msgs_to_send -= 1
                            if not msgs_to_send:
                                mapped_flag_holder[1] = True
                    except FreeMemoryChunkNotFoundError:
                        pass
                    finally:
                        mapped_flag_holder[0] = False

        while True:
            with wait_my_turn(sm):
                if mapped_flag_holder[0]:
                    mapped_flag_holder[0] = False
                    break

        print('Sender is done.')


if __name__ == '__main__':
    print('Sender is starting its work.')
    sender()
    print('Sender has finished its work.')
