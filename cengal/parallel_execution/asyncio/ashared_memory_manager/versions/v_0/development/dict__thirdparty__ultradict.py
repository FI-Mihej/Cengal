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

from UltraDict import UltraDict

from multiprocessing import Process, Manager
from enum import IntEnum, Enum
from typing import List, Dict, Any


class ControlFields(IntEnum):
    data_state = 0
    sender_ready = 1
    receiver_ready = 2
    players_num = 3
    iterations_num = 4
    sub_iterations_num = 5
    ultra_dict_name = 6


class ControlFieldsStr(Enum):
    data_state = 'data_state'
    sender_ready = 'sender_ready'
    receiver_ready = 'receiver_ready'
    players_num = 'players_num'
    iterations_num = 'iterations_num'
    sub_iterations_num = 'sub_iterations_num'
    ultra_dict_name = 'ultra_dict_name'


class ControlDataState(IntEnum):
    data_ready = 0
    processing_requested = 1
    processing_done = 2
    stop_system = 3


def receiver(control: List, shared_players: List[Dict]):
    pcen()

    while not control[ControlFields.sender_ready]:
        pass

    control_ultra_dict: Dict[ControlFields, Any] = UltraDict(name=control[ControlFields.ultra_dict_name])
    control = control_ultra_dict

    mapped_shared_players: List[Dict] = list()
    with MeasureTimeTraceLine('Mapping UltraDict instances', len(shared_players)) as mt:
        for ultra_dict_name in shared_players:
            mapped_shared_players.append(UltraDict(name=ultra_dict_name))
    
    control[ControlFieldsStr.receiver_ready.value] = True
    while ControlDataState.stop_system.value != control[ControlFieldsStr.data_state.value]:
        while control[ControlFieldsStr.data_state.value] not in {ControlDataState.processing_requested.value, ControlDataState.stop_system.value}:
            pass

        if ControlDataState.stop_system.value == control[ControlFieldsStr.data_state.value]:
            break

        try:
            sub_iterations_num: int = control[ControlFieldsStr.sub_iterations_num.value]
            for player_state in mapped_shared_players:
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
            control[ControlFieldsStr.data_state.value] = ControlDataState.processing_done.value
    
    print('Receiver - done.')


def sender(control: List, shared_players: List[Dict]):
    pcen()

    control[ControlFields.players_num] = 15000
    control[ControlFields.iterations_num] = 1
    control[ControlFields.sub_iterations_num] = 1
    ultra_dict_per_name: Dict[str, UltraDict] = dict()
    with MeasureTimeTraceLine('Creating UltraDict instances', control[ControlFields.players_num]) as mt:
        for player_id in range(mt.iterations):
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
            ultra_dict: UltraDict = UltraDict(player_state)
            shared_players.append(ultra_dict.name)
            ultra_dict_per_name[ultra_dict.name] = ultra_dict

    control_ultra_dict: Dict[ControlFields, Any] = UltraDict({
        ControlFieldsStr.data_state.value: control[ControlFields.data_state],
        ControlFieldsStr.sender_ready.value: control[ControlFields.sender_ready],
        ControlFieldsStr.receiver_ready.value: control[ControlFields.receiver_ready],
        ControlFieldsStr.players_num.value: control[ControlFields.players_num],
        ControlFieldsStr.iterations_num.value: control[ControlFields.iterations_num],
        ControlFieldsStr.sub_iterations_num.value: control[ControlFields.sub_iterations_num],
        ControlFieldsStr.ultra_dict_name.value: None,
    })
    control_ultra_dict_name = control_ultra_dict.name
    control_ultra_dict[ControlFields.ultra_dict_name] = control_ultra_dict_name
    control_ultra_dict[ControlFields.sender_ready] = True
    control[ControlFields.ultra_dict_name] = control_ultra_dict_name
    control[ControlFields.sender_ready] = True
    control = control_ultra_dict
    while not control[ControlFieldsStr.receiver_ready.value]:
        pass

    with MeasureTimeTraceLine('Data processing', control[ControlFieldsStr.iterations_num.value], line_type=LineType.relative_line, line_num=-2) as mt:
        for _ in range(mt.iterations):
            control[ControlFieldsStr.data_state.value] = ControlDataState.processing_requested.value
            while ControlDataState.processing_done.value != control[ControlFieldsStr.data_state.value]:
                pass
            
            # Reading data
            for ultra_dict_name, ultra_dict in ultra_dict_per_name.items():
                dict(ultra_dict)
    
    fields_per_player: int = len(ultra_dict_per_name[shared_players[0]]) - 2
    increments_num: int = mt.iterations * len(shared_players) * fields_per_player * control[ControlFieldsStr.sub_iterations_num.value]
    print(f'It took {mt.time_spent} seconds to made {increments_num} increments')
    increments_per_second: float = increments_num / mt.time_spent
    if mt.time_spent:
        print(f'There are {increments_per_second} increments/seconds')
    
    print()
    increments_num: int = mt.iterations * len(shared_players) * fields_per_player
    print(f'It took {mt.time_spent} seconds to adjust {increments_num} player fields')
    increments_per_second: float = increments_num / mt.time_spent
    if mt.time_spent:
        print(f'There are {increments_per_second} adjustments/seconds')

    print()
    increments_num: int = mt.iterations * len(shared_players)
    print(f'It took {mt.time_spent} seconds to update {increments_num} players')
    increments_per_second: float = increments_num / mt.time_spent
    if mt.time_spent:
        print(f'There are {increments_per_second} player_updates/seconds')

    print()
    print(dict(ultra_dict_per_name[shared_players[0]]))
    control[ControlFieldsStr.data_state.value] = ControlDataState.stop_system.value
    print('Sender - done.')


def main():
    with Manager() as manager:
        control = manager.list([ControlDataState.data_ready, False, False, None, None, None, None])
        shared_players = manager.list()

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
