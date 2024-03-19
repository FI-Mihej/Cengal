# CengalAppDirPathFinder

CengalAppDirPathFinder is a cross-platform Python module designed to simplify the process of locating OS-recommended directories for application data, cache, logs, and more. It seamlessly integrates with Windows, Linux, and macOS, utilizing platform-specific standards like `KNOWNFOLDERID constants` on Windows, `XDG standards` on Linux, and `NSSearchPathForDirectoriesInDomains` on macOS. This module offers a unified API for accessing various types of directories, such as local, roaming, and program-specific paths, enhancing application compatibility and data management across different operating systems.

# Installation

```bash
pip install cengal_app_dir_path_finder
```

# Documentation

## Import

```python
from cengal_app_dir_path_finder import AppDirectoryType, AppDirPath
```

## Usage

```python
import os
from cengal_app_dir_path_finder import AppDirectoryType, AppDirPath

app_dir_path: AppDirPath = AppDirPath()
local_data_dir_path: str = app_dir_path(AppDirectoryType.local_data, 'MyApplicationName')
settings_json_path: str = os.path.join(local_data_dir_path, 'settings.json')
with open(settings_json_path, 'w') as file:
    file.write(my_app_settings)
```

## Supported foler types

`AppDirectoryType` is an enum of all supported kinds of directories.

`AppDirectoryType` Fields:
* `local_data`: Local user-specific data storage, not shared across users, ideal for storing user preferences, game scores, etc.
* `local_low_data`: Low privilege local data storage for sandboxed or security-sensitive applications.
* `roaming_data`: User-specific data that may sync across devices, suitable for configurations and settings.
* `local_cache`: Stores temporary, user-specific cache data that can be regenerated as needed.
* `local_low_cache`: Similar to local_cache but for applications requiring lower access privileges.
* `roaming_cache`: User-specific cache data that could be shared and synced across devices.
* `local_temp`: Temporary files and data specific to the current user.
* `local_low_temp`: Temporary files for applications with lower privileges.
* `roaming_temp`: Temporary user-specific files that might be synced across devices.
* `local_log`: Logs and operation records for the current user.
* `local_low_log`: Logs for low privilege applications.
* `roaming_log`: User-specific logs that might be shared across devices.
* `local_config`: Configuration files and settings for the current user.
* `local_low_config`: Configuration for applications with lower privileges.
* `roaming_config`: Configurations that might be synced across a user's devices.
* `local_runtime`: User-specific runtime data like sockets and named pipes.
* `local_low_runtime`: Runtime data for applications with lower privileges.
* `roaming_runtime`: User-specific runtime data that could be synced across devices.
* `program_files`: Static data shared among all users, like application binaries.
* `program_files_common`: Shared libraries and common resources for multiple applications.
* `program_data`: Non-static data shared among users, like shared databases.
* `program_cache`: Cache for shared applications and services.
* `program_temp`: Temporary files for shared applications.
* `program_log`: Log files for system-wide applications.
* `program_config`: Configuration files for system-wide applications.
* `program_runtime`: System-wide runtime data like global sockets and named pipes.
* `user_profile_data`: User-specific application data within the user's home directory.
* `user_profile_program_files`: Static data specific to user-installed applications.
* `user_profile_program_files_common`: Shared resources for user-specific applications.
* `local_static_data`: Static data specific to the local user, not frequently modified.
* `local_low_static_data`: Static data for lower privilege user applications.
* `roaming_static_data`: User-specific static data that may sync across devices.
* `program_static_data`: Static data shared among all users and applications.

## AppDirPath methods

### `__call__(...)`

`def __call__(self, dir_type: AppDirectoryType, app_name_or_path: DirNameOrPath, with_structure: bool = True, ensure_dir: bool = True) -> str:`

Constructs path of the requestet directory type taking into account provided application name.
* `with_structure`:
    * `False`: determines base directory provided by OS and followed with an application name
    * `True`: determines base directory provided by OS, followed with an application name and completed with a suffixes like 'cache', 'config', 'log', etc.
* `ensure_dir`:
    * `True`: creates directory sequence if does not exists

### `cached(...)`

`def cached(self, dir_type: AppDirectoryType, app_name_or_path: DirNameOrPath, with_structure: bool = True, ensure_dir: bool = True) -> str:`

Cached version. Much faster in a repetitive requests.

## Global app instances of AppDirPath

An `Instance` service from the `Cengal.Coroutines` holds globally accessible instance of the AppDirPath as well as globally acessible field for an application name:

```python
{
    ...
    'app_name': str(),
    'app_name_for_fs': str(),
    'app_version': tuple(),
    'app_version_str': str(),
    AppDirPath: AppDirPath(),
    'app_data_dir_path_type': AppDirectoryType.local_data,
    'app_cache_dir_path_type': AppDirectoryType.local_cache,
    'app_temp_dir_path_type': AppDirectoryType.local_temp,
    'app_log_dir_path_type': AppDirectoryType.local_log,
    'app_config_dir_path_type': AppDirectoryType.local_config,
    'app_runtime_dir_path_type': AppDirectoryType.local_runtime,
    ...
}
```

Several `Cengal.Coroutines.Services` using these fields and instances in their work. For example such services as `db` (async LMDB) and `log`.

Short example of proper usage:

```python
from cengal_app_dir_path_finder import AppDirectoryType, AppDirPath
from cengal.parallel_execution.coroutines.coro_scheduler import cs_acoro
from cengal.parallel_execution.coroutines.coro_standard_services.instance import afast_wait, fast_get, fast_set
from uuid import uuid4


MY_APP_CONFIGURATION_COMPLETED_FLAG_NAME: str = f'My Application Mandatory Configuration Complited {uuid4()}'


@cs_acoro
async def set_app_name(app_name: str) -> None:
    fast_set('app_name_for_fs', app_name)
    fast_set(MY_APP_CONFIGURATION_COMPLETED_FLAG_NAME, None)


@cs_acoro
async def get_local_temp_dir() -> str:
    await afast_wait(MY_APP_CONFIGURATION_COMPLETED_FLAG_NAME)
    app_dir_path: AppDirPath = fast_get(AppDirPath)
    return app_dir_path.cached(fast_get('app_temp_dir_path_type'), fast_get('app_name_for_fs'))
```

Same example but a bit faster in an execution performance terms:

```python
from cengal.file_system.app_fs_structure.app_dir_path import AppDirectoryType, AppDirPath  # totaly the same import as in a previous example
from cengal.parallel_execution.coroutines.coro_scheduler import Interface
from cengal.parallel_execution.coroutines.coro_standard_services.instance import afast_wait_explicit, fast_get_explicit, fast_set_explicit
from uuid import uuid4


MY_APP_CONFIGURATION_COMPLETED_FLAG_NAME: str = f'My Application Mandatory Configuration Complited {uuid4()}'


async def set_app_name(i: Interface, app_name: str) -> None:
    fast_set_explicit(i, 'app_name_for_fs', app_name)
    fast_set_explicit(i, MY_APP_CONFIGURATION_COMPLETED_FLAG_NAME, None)


async def get_local_temp_dir(i: Interface) -> str:
    await afast_wait_explicit(i, MY_APP_CONFIGURATION_COMPLETED_FLAG_NAME)
    app_dir_path: AppDirPath = fast_get_explicit(i, AppDirPath)
    return app_dir_path.cached(fast_get_explicit(i, 'app_temp_dir_path_type'), 
        fast_get_explicit(i, 'app_name_for_fs'))
```

# Based on Cengal

Represents part of Cengal library:
* https://pypi.org/project/cengal/
* https://github.com/FI-Mihej/Cengal

An equivalent import:
```python
from cengal.file_system.app_fs_structure.app_dir_path import AppDirectoryType, AppDirPath
```

Cengal library can be installed by:

```bash
pip install cengal
```


# Projects using Cengal

* [flet_async](https://github.com/FI-Mihej/flet_async) - wrapper which makes [Flet](https://github.com/flet-dev/flet) async and brings booth Cengal.coroutines and asyncio to Flet (Flutter based UI)
* [justpy_containers](https://github.com/FI-Mihej/justpy_containers) - wrapper around [JustPy](https://github.com/justpy-org/justpy) in order to bring more security and more production-needed features to JustPy (VueJS based UI)
* [Bensbach](https://github.com/FI-Mihej/Bensbach) - decompiler from Unreal Engine 3 bytecode to a Lisp-like script and compiler back to Unreal Engine 3 bytecode. Made for a game modding purposes
* [Realistic-Damage-Model-mod-for-Long-War](https://github.com/FI-Mihej/Realistic-Damage-Model-mod-for-Long-War) - Mod for both the original XCOM:EW and the mod Long War. Was made with a Bensbach, which was made with Cengal
* [SmartCATaloguer.com](http://www.smartcataloguer.com/index.html) - TagDB based catalog of images (tags), music albums (genre tags) and apps (categories)

# License

Copyright © 2012-2024 ButenkoMS. All rights reserved.

Licensed under the Apache License, Version 2.0.