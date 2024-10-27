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
from cengal.text_processing.text_processing import to_identifier
from cengal.hardware.memory.shared_memory import *

from dataclasses import dataclass
from multiprocessing import Process, Manager
from os.path import basename
from enum import IntEnum
from typing import List, Dict


class ControlFields(IntEnum):
    data_state = 0
    receiver_ready = 1
    players_num = 2
    iterations_num = 3
    sub_iterations_num = 4


class ControlDataState(IntEnum):
    data_ready = 0
    processing_requested = 1
    processing_done = 2
    stop_system = 3


@dataclass
class Player:
    player_id: int
    player_name: str
    player_health: int
    player_mana: int
    player_position__x: float
    player_position__y: float
    player_position__z: float
    player_rotation__x: float
    player_rotation__y: float
    player_rotation__z: float
    player_inventory_size: int


player_incrementable_fields_num: int = 9


def receiver(shared_memory_name: str):
    pcen()
    with SharedMemory(shared_memory_name) as sm:
        sm.init_consumer()

        with wait_my_turn_when_has_messages(sm):
            mapped_control: List = sm.take_message()
            control: List = mapped_control

        with wait_my_turn_when_has_messages(sm):
            with MeasureTimeTraceLine('Mapping shared dict instances', control[ControlFields.players_num]) as mt:
                mapped_shared_players: List[Dict] = sm.take_message()
                shared_players: List[Dict] = mapped_shared_players
                shared_dict_per_index: Dict[int, Dict] = dict()
                for index, mapped_player in enumerate(mapped_shared_players):
                    shared_dict_per_index[index] = mapped_player
                
                shared_players = mapped_shared_players
            
            control[ControlFields.receiver_ready] = True

        stop_system: bool = False
        processing_requested: bool = False
        while not stop_system:
            while (not processing_requested) and (not stop_system):
                with wait_my_turn(sm, periodic_sleep_time=None):
                    processing_requested = ControlDataState.processing_requested.value == control[ControlFields.data_state]
                    stop_system = ControlDataState.stop_system.value == control[ControlFields.data_state]
                    if stop_system:
                        break

                    if processing_requested:
                        try:
                            sub_iterations_num: int = control[ControlFields.sub_iterations_num]
                            for _, player_state in shared_dict_per_index.items():
                                for _ in range(sub_iterations_num):
                                    k = player_state.player_health
                                    k = player_state.player_mana
                                    k = player_state.player_position__x
                                    k = player_state.player_position__y
                                    k = player_state.player_position__z
                                    k = player_state.player_rotation__x
                                    k = player_state.player_rotation__y
                                    k = player_state.player_rotation__z
                                    k = player_state.player_inventory_size
                        finally:
                            control[ControlFields.data_state] = ControlDataState.processing_done.value
                            processing_requested = False
    
    print('Receiver - done.')


def sender(shared_memory_name: str):
    pcen()
    with SharedMemory(shared_memory_name, True, 1000 * 1024**2) as sm:
        sm.wait_consumer_ready()
        with wait_my_turn(sm):
            control: List = intenum_dict_to_list({
                ControlFields.data_state: ControlDataState.data_ready,
                ControlFields.receiver_ready: False,
                ControlFields.players_num: 15000,
                ControlFields.iterations_num: 1,
                ControlFields.sub_iterations_num: 1,
            })
            mapped_control: List = sm.put_message(control)
            control = mapped_control
            
            shared_players: List[Dict] = list()
            shared_dict_per_index: Dict[int, Dict] = dict()
            with MeasureTimeTraceLine('Creating shared dict instances', control[ControlFields.players_num]) as mt:
                for player_id in range(mt.iterations):
                    player_state: Player = Player(
                        player_id=player_id,
                        player_name=f'Player_{player_id}',
                        player_health=100,
                        player_mana=100,
                        player_position__x=0.0,
                        player_position__y=0.0,
                        player_position__z=0.0,
                        player_rotation__x=0.0,
                        player_rotation__y=0.0,
                        player_rotation__z=0.0,
                        player_inventory_size=0,
                    )
                    shared_players.append(player_state)

                mapped_shared_players: List[Dict] = sm.put_message(shared_players)
                for index, mapped_player in enumerate(mapped_shared_players):
                    shared_dict_per_index[index] = mapped_player
                
                shared_players = mapped_shared_players

        receiver_ready: bool = False
        while not receiver_ready:
            with wait_my_turn(sm):
                receiver_ready = control[ControlFields.receiver_ready]
    
        with MeasureTimeTraceLine('Data processing', control[ControlFields.iterations_num], line_type=LineType.relative_line, line_num=-2) as mt:
            for _ in range(mt.iterations):
                with wait_my_turn(sm, periodic_sleep_time=None):
                    control[ControlFields.data_state] = ControlDataState.processing_requested.value

                processing_done: bool = False
                while not processing_done:
                    with wait_my_turn(sm, periodic_sleep_time=None):
                        processing_done = ControlDataState.processing_done.value == control[ControlFields.data_state]
                        # if processing_done:
                        #     # Reading data
                        #     for shared_dict_index, shared_dict in shared_dict_per_index.items():
                        #         k = player_state.player_health
                        #         k = player_state.player_mana
                        #         k = player_state.player_position__x
                        #         k = player_state.player_position__y
                        #         k = player_state.player_position__z
                        #         k = player_state.player_rotation__x
                        #         k = player_state.player_rotation__y
                        #         k = player_state.player_rotation__z
                        #         k = player_state.player_inventory_size
        
        fields_per_player: int = player_incrementable_fields_num
        increments_num: int = mt.iterations * len(shared_players) * fields_per_player * control[ControlFields.sub_iterations_num]
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
        # print(dict(shared_dict_per_index[0]))
        print(shared_dict_per_index[0])

        with wait_my_turn(sm):
            control[ControlFields.data_state] = ControlDataState.stop_system.value
        
        print('Sender - done.')


def main():
    with Manager() as manager:
        shared_memory_name: str = to_identifier(basename(__file__).replace('.', '_'))

        # Create and start processes
        process_receiver = Process(target=receiver, args=(shared_memory_name,))
        process_sender = Process(target=sender, args=(shared_memory_name,))

        process_receiver.start()
        process_sender.start()

        # Wait for processes to complete
        process_sender.join()
        process_receiver.join()


if __name__ == '__main__':
    ensure_adjusted_pythonhashseed()  # Ensure that the hash seed is adjusted for this process group
    # ensure_adjusted_scientific()  # Ensure (for this process group) that: 1) the hash seed is adjusted; 2) interpreter optimizations ('-OO') are turned on; 3) the integer string conversion length limitation is turned off
    main()
