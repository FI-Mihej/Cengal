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

__all__ = ['CallHistoryReapplier', 'CoroPriority']


from typing import Dict, Tuple, Hashable, Any
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import *


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


class CallHistoryReapplier:
    def __init__(self, priority: CoroPriority=CoroPriority.normal):
        self.history: Dict = dict()
        self.priority = priority
    
    def call_impl(self, *args, **kwargs):
        raise NotImplementedError
    
    def args_to_key_value(self, *args, **kwargs) -> Tuple[Hashable, Any]:
        raise NotImplementedError
    
    def key_value_to_args(self, key: Hashable, value: Any) -> Tuple[Tuple, Dict]:
        raise NotImplementedError
    
    def __call__(self, *args, **kwargs):
        key, value = self.args_to_key_value(*args, **kwargs)
        self.history[key] = value
        self.call_impl(*args, **kwargs)
    
    def reapply(self):
        ly = gly(self.priority)
        new_history = dict()
        while self.history:
            history_buff = self.history
            self.history = type(self.history)()
            for key, value in history_buff.items():
                args, kwargs = self.key_value_to_args(key, value)
                new_history[key] = value
                self.call_impl(*args, **kwargs)
                ly()
        
        # in order to not lose call history made in intermediate of the reapplying process:
        # self.history = new_history
        new_history.update(self.history)
        self.history = new_history

    def destroy(self):
        self.history = type(self.history)()
