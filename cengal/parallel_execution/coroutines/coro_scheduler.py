from greenlet import greenlet
from cengal.time_management.timer import Timer
from typing import Dict, Tuple, List, Callable, Any, Optional, Type


class Counter:
    def __init__(self):
        self._index = -1  # type: int

    def get(self) -> int:
        self._index += 1
        return self._index


class Iterable:
    def iteration(self):
        raise NotImplementedError


ServiceType = Type['Service']
ItemID = int
CoroID = ItemID
Worker = Callable[['WorkerInfo'], None]
Coro = greenlet


class CoroScheduler(Iterable):
    def __init__(self):
        self.root_coro_loop = greenlet(self._loop_imp)            # type: Coro
        self.root_coro_iteration = greenlet(self._iteration_imp)  # type: Coro
        self.root_coro = None                                     # type: Optional[Coro]
        self.services = dict()                                    # type: Dict[ServiceType, Service]
        self.requests = list()                                    # type: List[Request]
        self.responses = list()                                   # type: List[Response]
        self.new_born_coroutines = list()                         # type: List[CoroWrapper]
        self.coroutines = dict()                                  # type: Dict[CoroID, CoroWrapper]
        self.coro_counter = Counter()                             # type: Counter
        self.timer = Timer()

    def put_coro(self, coro_worker: Worker, *args, **kwargs) -> CoroID:
        coro_id = self.coro_counter.get()
        coro = CoroWrapper(self, coro_id, coro_worker, *args, **kwargs)
        self.new_born_coroutines.append(coro)
        return coro_id

    def register_service(self, service_type: ServiceType) -> bool:
        if service_type in self.services:
            return False
        else:
            self.services[service_type] = service_type(self)
            return True

    def loop(self):
        self.root_coro = self.root_coro_loop
        self.root_coro.switch()
        self.root_coro = None
        self.root_coro_loop = greenlet(self._loop_imp)

    def _loop_imp(self):
        while self.new_born_coroutines or self.coroutines:
            self._iteration_imp()

    def iteration(self):
        self.root_coro = self.root_coro_iteration
        self.root_coro.switch()
        self.root_coro = None
        self.root_coro_iteration = greenlet(self._iteration_imp)

    def _iteration_imp(self):
        self.timer()
        new_born_coroutines_buff = self.new_born_coroutines
        self.new_born_coroutines = type(self.new_born_coroutines)()
        for coro in new_born_coroutines_buff:
            coro: CoroWrapper = coro
            coro_id = coro.coro_id
            request = coro.init(self.root_coro)
            if request is not None:
                self.requests.append(request)
                self.coroutines[coro_id] = coro
            self.timer()

        self.timer()
        responses_buff = self.responses
        self.responses = type(self.responses)()
        for response in responses_buff:
            coro_id = response.coro_id
            if coro_id not in self.coroutines:
                continue
            coro = self.coroutines[coro_id]
            request = coro(response)
            if request is None:
                del self.coroutines[coro_id]
            else:
                self.requests.append(request)
            self.timer()

        self.timer()
        requests_buff = self.requests
        self.requests = type(self.requests)()
        for request in requests_buff:
            self.services[request.service_id].put_task(request)
            self.timer()

        for service_id, service in self.services.items():
            results = service.iteration()
            if results is not None:
                self.responses.extend(results)
            self.timer()

    def put_task(self, coro_id: CoroID, service_id: ServiceType, *args, **kwargs) -> 'Response':
        """
        Should be called from inside coroutines only.
        Will request some long running work to some service.

        :param coro_id:
        :param service_id:
        :param args:
        :param kwargs:
        """

        request: Request = Request(coro_id, service_id, *args, **kwargs)
        response: Response = self.root_coro.switch(request)
        return response


class Request:
    def __init__(self, coro_id: CoroID, service_id: ServiceType, *args, **kwargs):
        self.coro_id = coro_id
        self.service_id = service_id
        self.args = args
        self.kwargs = kwargs


class Response:
    def __init__(self, coro_id: CoroID, service_id: ServiceType, response: Any):
        self.coro_id = coro_id
        self.service_id = service_id
        self.response = response

    def __call__(self) -> Any:
        return self.response


class CoroWrapper:
    def __init__(self, loop: CoroScheduler, coro_id: CoroID, worker: Worker, *args, **kwargs):
        self.init_args = args      # type: Tuple[Any, ...]
        self.init_kwargs = kwargs  # type: Dict
        self.coro_id = coro_id     # type: CoroID
        self.worker = worker       # type: Worker
        self.loop = loop           # type: CoroScheduler
        self.coro = None           # type: Optional[Coro]

    def init(self, parent_coro: Optional[Coro] = None) -> Optional[Request]:
        self.coro = greenlet(self.worker, parent_coro)
        result = self.coro.switch(Interface(self.loop, self.coro_id), *self.init_args, **self.init_kwargs)
        return result

    def __call__(self, *args, **kwargs) -> Optional[Request]:
        result = self.coro.switch(*args, **kwargs)
        return result


class Interface:
    def __init__(self, loop: CoroScheduler, coro_id: CoroID):
        self.__loop = loop
        self.coro_id = coro_id

    def __call__(self, service_id: ServiceType, *args, **kwargs) -> Any:
        """
        Should be called from inside coroutines only.
        Will request some long running work to some service.

        :param coro_id:
        :param service_id:
        :param args:
        :param kwargs:
        """

        response = self.__loop.put_task(self.coro_id, service_id, *args, *kwargs)
        return response()

    def put_coro(self, coro_worker: Worker, *args, **kwargs) -> CoroID:
        coro_id = self.__loop.put_coro(coro_worker, *args, **kwargs)
        return coro_id


class CallerCoroInfo:
    def __init__(self, coro_id: CoroID):
        self.coro_id = coro_id


class Service(Iterable):
    def __init__(self, loop: CoroScheduler):
        super(Service, self).__init__()
        self._loop = loop                     # type: CoroScheduler
        self._requests = list()               # type: List[Request]
        self._responses = list()              # type: List[Response]
        self.current_caller_coro_info = None  # type: Optional[CallerCoroInfo]

    def iteration(self) -> Optional[List[Response]]:
        requests = self._requests
        self._requests = type(self._requests)()
        self._responses = list()
        for request in requests:
            self.current_caller_coro_info = CallerCoroInfo(request.coro_id)
            result_exists, result = \
                self.single_task_registration_or_immediate_processing(*request.args, **request.kwargs)
            if result_exists:
                self.register_response(request.coro_id, result)
        self.current_caller_coro_info = None
        self.full_processing_iteration()
        return self._responses

    def register_response(self, coro_id: CoroID, response: Any):
        self._responses.append(Response(coro_id, type(self), response))

    def put_task(self, request: Request):
        self._requests.append(request)

    def single_task_registration_or_immediate_processing(self, *args, **kwargs) -> Tuple[bool, Any]:
        raise NotImplementedError

    def full_processing_iteration(self):
        raise NotImplementedError

    def in_work(self) -> bool:
        raise NotImplementedError
