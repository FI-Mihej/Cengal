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
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.performance_test_lib import MeasureTimeTraceLine, LineType
from cengal.introspection.inspect import pcen

from multiprocessing import Process, Manager
from enum import IntEnum
from typing import List, Dict


class ControlFields(IntEnum):
    data_state = 0
    sender_ready = 1
    receiver_ready = 2
    players_num = 3
    iterations_num = 4
    sub_iterations_num = 5


class ControlDataState(IntEnum):
    data_ready = 0
    processing_requested = 1
    processing_done = 2
    stop_system = 3


def receiver(control: List, shared_players: List[Dict]):
    pcen()

    while not control[ControlFields.sender_ready]:
        pass

    shared_dict_per_index: Dict[int, Dict] = dict()
    for index, mapped_player in enumerate(shared_players):
        shared_dict_per_index[index] = mapped_player
    
    control[ControlFields.receiver_ready] = True
    while ControlDataState.stop_system.value != control[ControlFields.data_state]:
        while control[ControlFields.data_state] not in {ControlDataState.processing_requested.value, ControlDataState.stop_system.value}:
            pass

        if ControlDataState.stop_system.value == control[ControlFields.data_state]:
            break

        try:
            sub_iterations_num: int = control[ControlFields.sub_iterations_num]
            for _, player_state in shared_dict_per_index.items():
                for _ in range(sub_iterations_num):
                    player_state['player_health'] += 1
                    player_state['player_mana'] += 1
                    player_state['player_position__x'] += 1.0
                    player_state['player_position__y'] += 1.0
                    player_state['player_position__z'] += 1.0
                    player_state['player_rotation__x'] += 1.0
                    player_state['player_rotation__y'] += 1.0
                    player_state['player_rotation__z'] += 1.0
                    player_state['player_inventory_size'] += 1
        finally:
            control[ControlFields.data_state] = ControlDataState.processing_done.value
    
    print('Receiver - done.')


def sender(control: List, shared_players: List[Dict]):
    pcen()
    control[ControlFields.sender_ready] = True
    while not control[ControlFields.receiver_ready]:
        pass

    with MeasureTimeTraceLine('Data processing', control[ControlFields.iterations_num], line_type=LineType.relative_line, line_num=-2) as mt:
        for _ in range(mt.iterations):
            control[ControlFields.data_state] = ControlDataState.processing_requested.value
            while ControlDataState.processing_done.value != control[ControlFields.data_state]:
                pass
    
    increments_num: int = mt.iterations * len(shared_players) * (len(shared_players[0]) - 2) * control[ControlFields.sub_iterations_num]
    print(f'It was used {mt.time_spent} seconds to made {increments_num} increments')
    increments_per_second: float = increments_num / mt.time_spent
    if mt.time_spent:
        print(f'There is {increments_per_second} increments/seconds')
    
    print()
    increments_num: int = mt.iterations * len(shared_players) * (len(shared_players[0]) - 2)
    print(f'It was used {mt.time_spent} seconds to adjust {increments_num} player fields')
    increments_per_second: float = increments_num / mt.time_spent
    if mt.time_spent:
        print(f'There is {increments_per_second} adjustments/seconds')

    print()
    increments_num: int = mt.iterations * len(shared_players)
    print(f'It was used {mt.time_spent} seconds to update {increments_num} players')
    increments_per_second: float = increments_num / mt.time_spent
    if mt.time_spent:
        print(f'There is {increments_per_second} player_updates/seconds')

    print()
    print(dict(shared_players[0]))
    control[ControlFields.data_state] = ControlDataState.stop_system.value
    print('Sender - done.')


def main():
    with Manager() as manager:
        control = manager.list([ControlDataState.data_ready, False, False, 100, 1, 5])
        players: List[Dict] = list()
        for player_id in range(control[ControlFields.players_num]):
            player_state = {
                'player_id': player_id,
                'player_name': f'Player_{player_id}',
                'player_health': 100,
                'player_mana': 100,
                'player_position__x': 0.0,
                'player_position__y': 0.0,
                'player_position__z': 0.0,
                'player_rotation__x': 0.0,
                'player_rotation__y': 0.0,
                'player_rotation__z': 0.0,
                'player_inventory_size': 0,
            }
            players.append(manager.dict(player_state))
        
        shared_players = manager.list(players)

        # Create and start processes
        process_receiver = Process(target=receiver, args=(control, shared_players))
        process_sender = Process(target=sender, args=(control, shared_players))

        process_receiver.start()
        process_sender.start()

        # Wait for processes to complete
        process_sender.join()
        process_receiver.join()

if __name__ == '__main__':
    main()
