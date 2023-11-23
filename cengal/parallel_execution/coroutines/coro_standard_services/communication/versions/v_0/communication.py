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
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


__all__ = ['Communication']

from cengal.parallel_execution.coroutines.coro_scheduler import *
from enum import Enum
from typing import Hashable, NoReturn, Dict, Tuple, Any


class Communication(Service):

    class Requests(Enum):
        send_async = 0        # Coro will get control immediately after message sent
        send_sync = 1         # Coro will get control only after response will be received
        read_async = 2        # Coro will get control immediately even if input queue is empty
        read_sync = 3         # Coro will get control only if input queue is not empty or when new response will be
        # received
        named_send_async = 4  # Coro will get control immediately after message sent
        named_send_sync = 5   # Coro will get control only after response will be received
        named_read_async = 6  # Coro will get control immediately even if input queue is empty
        named_read_sync = 7   # Coro will get control only if input queue is not empty or when new response will be
        # received

    class Request:
        def __init__(self):
            self.request_type = None  # type: Optional[int]
            self.args = None          # type: Optional[Tuple]
            self.kwargs = None        # type: Optional[Dict]

        def send_async(self, recipient_id: CoroID, message: Any) -> 'Communication.Request':
            self._save(0, recipient_id, message)
            return self

        def send_blocking(self, recipient_id: CoroID, message: Any) -> 'Communication.Request':
            self._save(1, recipient_id, message)
            return self

        def read_async(self) -> 'Communication.Request':
            self._save(2)
            return self

        def read_blocking(self) -> 'Communication.Request':
            self._save(3)
            return self

        def send_async_named(
                self, sender_id: Hashable, recipient_id: Hashable, message: Any) -> 'Communication.Request':
            self._save(4, sender_id, recipient_id, message)
            return self

        def send_blocking_named(
                self, sender_id: Hashable, recipient_id: Hashable, message: Any) -> 'Communication.Request':
            self._save(5, sender_id, recipient_id, message)
            return self

        def read_async_named(self, recipient_id: Hashable) -> 'Communication.Request':
            self._save(6, recipient_id)
            return self

        def read_blocking_named(self, recipient_id: Hashable) -> 'Communication.Request':
            self._save(7, recipient_id)
            return self

        def _save(self, __request__type__: int, *args, **kwargs):
            self.request_type = __request__type__
            self.args = args
            self.kwargs = kwargs

    def __init__(self, loop: CoroScheduler):
        super(Communication, self).__init__(loop)

    def single_task_registration_or_immediate_processing(
            self, request: 'Communication.Requests', *args, **kwargs
    ) -> Tuple[bool, Any]:
        if 0 == request.request_type:
            self.request_send_async(*args, **kwargs)
            return True, None, None
        elif 1 == request.request_type:
            self.request_send_sync(*args, **kwargs)
            return False, None, None
        elif 2 == request.request_type:
            result = self.request_read_async()
            return True, result, None
        elif 3 == request.request_type:
            self.request_read_sync()
            return False, None, None
        elif 4 == request.request_type:
            self.request_named_send_async(*args, **kwargs)
            return True, None, None
        elif 5 == request.request_type:
            self.request_named_send_sync(*args, **kwargs)
            return False, None, None
        elif 6 == request.request_type:
            result = self.request_named_read_async(*args, **kwargs)
            return True, result, None
        elif 7 == request.request_type:
            self.request_named_read_sync(*args, **kwargs)
            return False, None, None

    def request_send_async(self, recipient_id: CoroID, message: Any) -> NoReturn:
        raise NotImplementedError

    def request_send_sync(self, recipient_id: CoroID, message: Any) -> NoReturn:
        raise NotImplementedError

    def request_read_async(self) -> Tuple[CoroID, Any]:
        """
        Will return tuple with sender coro ID and message

        :rtype: Tuple[CoroID, Any]
        """
        raise NotImplementedError

    def request_read_sync(self) -> NoReturn:
        raise NotImplementedError

    def request_named_send_async(self, sender_id: Hashable, recipient_id: Hashable, message: Any) -> NoReturn:
        raise NotImplementedError

    def request_named_send_sync(self, sender_id: Hashable, recipient_id: Hashable, message: Any) -> NoReturn:
        raise NotImplementedError

    def request_named_read_async(self, recipient_id: Hashable) -> Tuple[Hashable, Any]:
        """
        Will return tuple with sender ID and message

        :rtype: Tuple[Hashable, Any]
        """
        raise NotImplementedError

    def request_named_read_sync(self, recipient_id: Hashable) -> NoReturn:
        raise NotImplementedError

    def full_processing_iteration(self):
        pass

    def in_work(self) -> bool:
        return self.thrifty_in_work(False)
