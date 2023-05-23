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

from typing import Any, Dict, Hashable

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


VarName = str
VarValue = Any
MeasurementId = int
StageId = Hashable

class State:
    def add(self, var_name: VarName, var_value: VarValue, stage_id: StageId = None):
        raise NotImplementedError
    
    def add_set(self, vars: Dict[VarName, VarValue]):
        raise NotImplementedError
    
    def check_var(self, var_name: VarName):
        raise NotImplementedError
    
    def check_var_measurement(self, var_name: VarName, measurement_id_from: MeasurementId, measuremente_id_up_to: MeasurementId):
        raise NotImplementedError
    
    def check_var_current_state(self, var_name: VarName):
        raise NotImplementedError
    
    def check_all(self):
        raise NotImplementedError
    
    def check_all_current_state(self):
        raise NotImplementedError
