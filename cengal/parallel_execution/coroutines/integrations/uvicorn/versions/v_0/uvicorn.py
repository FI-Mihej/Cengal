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


__all__ = ['get_uvicorn_awaitable']


from uvicorn.main import *
from h11._connection import DEFAULT_MAX_INCOMPLETE_EVENT_SIZE


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


class UvicornStartupFailureError(Exception):
    pass


def get_uvicorn_awaitable(
    app: typing.Union["ASGIApplication", typing.Callable, str],
    *,
    host: str = "127.0.0.1",
    port: int = 8000,
    uds: typing.Optional[str] = None,
    fd: typing.Optional[int] = None,
    loop: LoopSetupType = "auto",
    http: typing.Union[typing.Type[asyncio.Protocol], HTTPProtocolType] = "auto",
    ws: typing.Union[typing.Type[asyncio.Protocol], WSProtocolType] = "auto",
    ws_max_size: int = 16777216,
    ws_ping_interval: typing.Optional[float] = 20.0,
    ws_ping_timeout: typing.Optional[float] = 20.0,
    ws_per_message_deflate: bool = True,
    lifespan: LifespanType = "auto",
    interface: InterfaceType = "auto",
    reload: bool = False,
    reload_dirs: typing.Optional[typing.Union[typing.List[str], str]] = None,
    reload_includes: typing.Optional[typing.Union[typing.List[str], str]] = None,
    reload_excludes: typing.Optional[typing.Union[typing.List[str], str]] = None,
    reload_delay: float = 0.25,
    workers: typing.Optional[int] = None,
    env_file: typing.Optional[typing.Union[str, os.PathLike]] = None,
    log_config: typing.Optional[
        typing.Union[typing.Dict[str, typing.Any], str]
    ] = LOGGING_CONFIG,
    log_level: typing.Optional[typing.Union[str, int]] = None,
    access_log: bool = True,
    proxy_headers: bool = True,
    server_header: bool = True,
    date_header: bool = True,
    forwarded_allow_ips: typing.Optional[typing.Union[typing.List[str], str]] = None,
    root_path: str = "",
    limit_concurrency: typing.Optional[int] = None,
    backlog: int = 2048,
    limit_max_requests: typing.Optional[int] = None,
    timeout_keep_alive: int = 5,
    ssl_keyfile: typing.Optional[str] = None,
    ssl_certfile: typing.Optional[typing.Union[str, os.PathLike]] = None,
    ssl_keyfile_password: typing.Optional[str] = None,
    ssl_version: int = SSL_PROTOCOL_VERSION,
    ssl_cert_reqs: int = ssl.CERT_NONE,
    ssl_ca_certs: typing.Optional[str] = None,
    ssl_ciphers: str = "TLSv1",
    headers: typing.Optional[typing.List[typing.Tuple[str, str]]] = None,
    use_colors: typing.Optional[bool] = None,
    app_dir: typing.Optional[str] = None,
    factory: bool = False,
    h11_max_incomplete_event_size: int = DEFAULT_MAX_INCOMPLETE_EVENT_SIZE,
) -> None:
    reload = False
    workers = None

    if app_dir is not None:
        sys.path.insert(0, app_dir)

    config = Config(
        app,
        host=host,
        port=port,
        uds=uds,
        fd=fd,
        loop=loop,
        http=http,
        ws=ws,
        ws_max_size=ws_max_size,
        ws_ping_interval=ws_ping_interval,
        ws_ping_timeout=ws_ping_timeout,
        ws_per_message_deflate=ws_per_message_deflate,
        lifespan=lifespan,
        interface=interface,
        reload=reload,
        reload_dirs=reload_dirs,
        reload_includes=reload_includes,
        reload_excludes=reload_excludes,
        reload_delay=reload_delay,
        workers=workers,
        env_file=env_file,
        log_config=log_config,
        log_level=log_level,
        access_log=access_log,
        proxy_headers=proxy_headers,
        server_header=server_header,
        date_header=date_header,
        forwarded_allow_ips=forwarded_allow_ips,
        root_path=root_path,
        limit_concurrency=limit_concurrency,
        backlog=backlog,
        limit_max_requests=limit_max_requests,
        timeout_keep_alive=timeout_keep_alive,
        ssl_keyfile=ssl_keyfile,
        ssl_certfile=ssl_certfile,
        ssl_keyfile_password=ssl_keyfile_password,
        ssl_version=ssl_version,
        ssl_cert_reqs=ssl_cert_reqs,
        ssl_ca_certs=ssl_ca_certs,
        ssl_ciphers=ssl_ciphers,
        headers=headers,
        use_colors=use_colors,
        factory=factory,
        h11_max_incomplete_event_size=h11_max_incomplete_event_size,
    )
    server = Server(config=config)

    async def uvicorn_awaitable():
        await server.serve()

        if config.uds and os.path.exists(config.uds):
            os.remove(config.uds)  # pragma: py-win32

        if not server.started and not config.should_reload and config.workers == 1:
            raise UvicornStartupFailureError
    
    return uvicorn_awaitable()
