from cengal.coroutines.coro_scheduler import *
from typing import Hashable, NoReturn
from enum import Enum


class SomePrinter(Service):
    def single_task_registration_or_immediate_processing(
            self, *args, **kwargs) -> Tuple[bool, None]:
        print(*args, **kwargs)
        return True, None

    def full_processing_iteration(self):
        pass

    def in_work(self) -> bool:
        return False


class CoroRunner(Service):
    def single_task_registration_or_immediate_processing(
            self, coro_worker: Worker, *args, **kwargs) -> Tuple[bool, CoroID]:
        coro_id = self._loop.put_coro(coro_worker, *args, **kwargs)
        return True, coro_id

    def full_processing_iteration(self):
        pass

    def in_work(self) -> bool:
        return False


class Yield(Service):
    def single_task_registration_or_immediate_processing(self) -> Tuple[bool, None]:
        return True, None

    def full_processing_iteration(self):
        pass

    def in_work(self) -> bool:
        return False


class Sleep(Service):
    def __init__(self, loop: CoroScheduler):
        super(Sleep, self).__init__(loop)
        self.timer = Timer()
        self.pending_tasks_number = 0

    def single_task_registration_or_immediate_processing(
            self, delay: float) -> Tuple[bool, Optional[float]]:
        def timer_handler_func(coro_id: CoroID, start_time: float):
            current_time = perf_counter()
            if start_time > current_time:
                start_time = current_time
            real_delay = current_time - start_time
            self.task_triggered()
            self.register_response(coro_id, real_delay)

        handler = partial(timer_handler_func, self.current_caller_coro_info.coro_id, perf_counter())
        self.task_added()
        self.timer.register(handler, delay)
        return False, None

    def full_processing_iteration(self):
        self.timer()

    def task_added(self):
        self.pending_tasks_number += 1

    def task_triggered(self):
        self.pending_tasks_number -= 1

    def in_work(self) -> bool:
        return self.pending_tasks_number != 0


class TimerFuncRunner(Service):
    def __init__(self, loop: CoroScheduler):
        super(TimerFuncRunner, self).__init__(loop)
        self.timer = Timer()
        self.pending_tasks_number = 0

    def single_task_registration_or_immediate_processing(
            self, delay: float, handler: Callable, *args, **kwargs) -> Tuple[bool, None]:
        def timer_handler_func(handler_: Callable, *args_, **kwargs_):
            handler_(*args_, **kwargs_)
            self.task_triggered()

        timer_handler = partial(timer_handler_func, handler, *args, **kwargs)
        self.task_added()
        self.timer.register(timer_handler, delay)
        return True, None

    def full_processing_iteration(self):
        self.timer()

    def task_added(self):
        self.pending_tasks_number += 1

    def task_triggered(self):
        self.pending_tasks_number -= 1

    def in_work(self) -> bool:
        return self.pending_tasks_number != 0


class TimerCoroRunner(Service):
    def __init__(self, loop: CoroScheduler):
        super(TimerCoroRunner, self).__init__(loop)
        self.timer = Timer()
        self.pending_tasks_number = 0

    def single_task_registration_or_immediate_processing(
            self, delay: float, coro_worker: Worker, *args, **kwargs) -> Tuple[bool, None]:
        def timer_handler_func(coro_worker_: Worker, *args_, **kwargs_):
            self._loop.put_coro(coro_worker_, *args_, **kwargs_)
            self.task_triggered()

        timer_handler = partial(timer_handler_func, coro_worker, *args, **kwargs)
        self.task_added()
        self.timer.register(timer_handler, delay)
        return True, None

    def full_processing_iteration(self):
        self.timer()

    def task_added(self):
        self.pending_tasks_number += 1

    def task_triggered(self):
        self.pending_tasks_number -= 1

    def in_work(self) -> bool:
        return self.pending_tasks_number != 0


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
            self.args = None          # type: Optional[Set]
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
            self, request: 'Communication.Requests', *args, **kwargs) -> Tuple[bool, Any]:
        if 0 == request.request_type:
            self.request_send_async(*args, **kwargs)
            return True, None
        elif 1 == request.request_type:
            self.request_send_sync(*args, **kwargs)
            return False, None
        elif 2 == request.request_type:
            result = self.request_read_async()
            return True, result
        elif 3 == request.request_type:
            self.request_read_sync()
            return False, None
        elif 4 == request.request_type:
            self.request_named_send_async(*args, **kwargs)
            return True, None
        elif 5 == request.request_type:
            self.request_named_send_sync(*args, **kwargs)
            return False, None
        elif 6 == request.request_type:
            result = self.request_named_read_async(*args, **kwargs)
            return True, result
        elif 7 == request.request_type:
            self.request_named_read_sync(*args, **kwargs)
            return False, None

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
        pass
