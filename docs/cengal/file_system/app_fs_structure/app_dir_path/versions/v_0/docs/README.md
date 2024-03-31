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

* Static Data. Your user-specific static data such as application's icons, static text or non-executable binary files, etc.:
    * `local_static_data`: Static data specific to the local user, not frequently modified.
    * `local_low_static_data`: Static data for lower privilege user applications.
    * `roaming_static_data`: User-specific static data that may sync across devices.
    * `program_static_data`: Static data shared among all users and applications.

* Local Data. Your main user-specific data storage:
    * `local_data`: Local user-specific data storage, not shared across users, ideal for storing user preferences, game scores, etc.
    * `local_cache`: Stores temporary, user-specific cache data that can be regenerated as needed.
    * `local_config`: Configuration files and settings for the current user.
    * `local_log`: Logs and operation records for the current user.
    * `local_temp`: Temporary files and data specific to the current user.
    * `local_runtime`: User-specific runtime data like sockets and named pipes.

* System-wide Data. For system services and other hi privilege applications:
    * `program_data`: Non-static data shared among users, like shared databases.
    * `program_cache`: Cache for shared applications and services.
    * `program_config`: Configuration files for system-wide applications.
    * `program_log`: Log files for system-wide applications.
    * `program_temp`: Temporary files for shared applications.
    * `program_runtime`: System-wide runtime data like global sockets and named pipes.

* Local Low Data. User-specific low privilege local data storage for sandboxed or security-sensitive applications. For example for web browsers:
    * `local_low_data`: Low privilege local data storage for sandboxed or security-sensitive applications.
    * `local_low_cache`: Similar to local_cache but for applications requiring lower access privileges.
    * `local_low_config`: Configuration for applications with lower privileges.
    * `local_low_log`: Logs for low privilege applications.
    * `local_low_temp`: Temporary files for applications with lower privileges.
    * `local_low_runtime`: Runtime data for applications with lower privileges.

* Roaming Data. User-specific data that may sync across devices:
    * `roaming_data`: User-specific data that may sync across devices, suitable for configurations and settings.
    * `roaming_cache`: User-specific cache data that could be shared and synced across devices.
    * `roaming_config`: Configurations that might be synced across a user's devices.
    * `roaming_log`: User-specific logs that might be shared across devices.
    * `roaming_temp`: Temporary user-specific files that might be synced across devices.
    * `roaming_runtime`: User-specific runtime data that could be synced across devices.

* `program_files`: Static data shared among all users, like application binaries.
* `program_files_common`: Shared libraries and common resources for multiple applications.

* `user_profile_data`: User-specific application data within the user's home directory. (`/home/<Username>/.<ApplicationName>` in case of Linux)
* `user_profile_program_files`: Static data specific to user-installed applications. Executable files, etc.
* `user_profile_program_files_common`: Shared resources for user-specific applications. Shared libraries, components, etc.

## Static data

### Short Description

* `Purpose`: To store data that remains unchanged throughout the application's lifecycle. This includes configuration files, default settings, templates, and read-only resources that are essential for the application's operation but do not require modification or updates after the initial deployment.
* `Use Case`: Particularly valuable for applications that rely on a set of immutable resources for functionality—such as image editing software that includes a library of default filters and effects, or a document processing application that uses a collection of templates for various document types. This ensures that these resources are available to the application regardless of user-specific data or settings, providing a consistent foundation upon which the application's features and functionalities operate.

### Windows Folders

* `local_static_data`: Stores static data that doesn't change during the application lifecycle and doesn't need to roam.
    * KNOWNFOLDERID of the base directory: `FOLDERID_LocalAppData`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\Local\<ApplicationName>\static_data`
        * `with_structure=False`: `C:\Users\<Username>\AppData\Local\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\Local`
* `local_low_static_data`: Static data for lower privilege user applications.
    * KNOWNFOLDERID of the base directory: `FOLDERID_LocalAppDataLow`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\LocalLow\<ApplicationName>\static_data`
        * `with_structure=False`: `C:\Users\<Username>\AppData\LocalLow\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\LocalLow`
* `roaming_static_data`: Similar to roaming_data but specifically for static data that should be available across sessions and machines.
    * KNOWNFOLDERID of the base directory: `FOLDERID_RoamingAppData`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\Roaming\<ApplicationName>\static_data`
        * `with_structure=False`: `C:\Users\<Username>\AppData\Roaming\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\Roaming`
* `program_static_data`: Stores static data similar to program_data, but explicitly indicates its static nature.
    * KNOWNFOLDERID of the base directory: `FOLDERID_ProgramData`
    * Examples:
        * `with_structure=True`: `C:\ProgramData\<ApplicationName>\static_data`
        * `with_structure=False`: `C:\ProgramData\<ApplicationName>`
        * `app_name_or_path=None`: `C:\ProgramData`

### Linux Folders

* `local_static_data`: Stores static data that doesn't change during the application lifecycle and doesn't need to roam.
    * Base directory: `os.environ.get('XDG_DATA_HOME', os.path.join(os.path.expanduser('~'), '.local', 'share'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.local/share/<ApplicationName>/local/static_data`
        * `with_structure=False`: `/home/<Username>/.local/share/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.local/share`
* `local_low_static_data`: Static data for lower privilege user applications.
    * Base directory: `os.environ.get('XDG_DATA_HOME', os.path.join(os.path.expanduser('~'), '.local', 'share'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.local/share/<ApplicationName>/local_low/static_data`
        * `with_structure=False`: `/home/<Username>/.local/share/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.local/share`
* `roaming_static_data`: Similar to roaming_data but specifically for static data that should be available across sessions and machines.
    * Base directory: `os.environ.get('XDG_DATA_HOME', os.path.join(os.path.expanduser('~'), '.local', 'share'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.local/share/<ApplicationName>/roaming/static_data`
        * `with_structure=False`: `/home/<Username>/.local/share/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.local/share`
* `program_static_data`: Stores static data similar to program_data, but explicitly indicates its static nature.
    * Base directory: `'/usr/share'`
    * Examples:
        * `with_structure=True`: `/usr/share/<ApplicationName>/static_data`
        * `with_structure=False`: `/usr/share/<ApplicationName>`
        * `app_name_or_path=None`: `/usr/share`

### macOS Folders

* `local_static_data`: Stores static data that doesn't change during the application lifecycle and doesn't need to roam.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Application Support/<ApplicationName>/local/static_data`
        * `with_structure=False`: `/Users/<Username>/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Application Support`
* `local_low_static_data`: Static data for lower privilege user applications.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Application Support/<ApplicationName>/local_low/static_data`
        * `with_structure=False`: `/Users/<Username>/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Application Support`
* `roaming_static_data`: Similar to roaming_data but specifically for static data that should be available across sessions and machines.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Application Support/<ApplicationName>/roaming/static_data`
        * `with_structure=False`: `/Users/<Username>/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Application Support`
* `program_static_data`: Stores static data similar to program_data, but explicitly indicates its static nature.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `localDomainMask`
    * Examples:
        * `with_structure=True`: `/Library/Application Support/<ApplicationName>/static_data`
        * `with_structure=False`: `/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Library/Application Support`

## Local App Data

### Short Description

* `Purpose`: To store user-specific application data that is local to a machine. Ideal for data that is too large to roam or that is only relevant to the specific device.
* `Use Case`: Commonly used for storing temporary files, cache, application logs, and other user-specific data that does not need to be synced across multiple devices.

### Windows Folders

* `local_data`: Stores application data that doesn't roam with the user. Typically used for storing large datasets or files that are specific to a machine.
    * KNOWNFOLDERID of the base directory: `FOLDERID_LocalAppData`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\Local\<ApplicationName>\data`
        * `with_structure=False`: `C:\Users\<Username>\AppData\Local\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\Local`
* `local_cache`: Used for storing temporary files that enhance application startup and operation. Cache files can be deleted without affecting application functionality.
    * KNOWNFOLDERID of the base directory: `FOLDERID_LocalAppData`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\Local\<ApplicationName>\cache`
        * `with_structure=False`: `C:\Users\<Username>\AppData\Local\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\Local`
* `local_config`: Stores configuration files. These files usually include settings that are specific to the machine.
    * KNOWNFOLDERID of the base directory: `FOLDERID_LocalAppData`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\Local\<ApplicationName>\config`
        * `with_structure=False`: `C:\Users\<Username>\AppData\Local\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\Local`
* `local_log`: Used for storing log files generated by the application. Useful for troubleshooting and monitoring application behavior.
    * KNOWNFOLDERID of the base directory: `FOLDERID_LocalAppData`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\Local\<ApplicationName>\log`
        * `with_structure=False`: `C:\Users\<Username>\AppData\Local\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\Local`
* `local_temp`: Intended for temporary files that are needed during the application's execution but not beyond that. These files can be cleared to free up space.
    * KNOWNFOLDERID of the base directory: `FOLDERID_LocalAppData`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\Local\<ApplicationName>\temp`
        * `with_structure=False`: `C:\Users\<Username>\AppData\Local\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\Local`
* `local_runtime`: Stores files required by the application at runtime. These could include dynamic libraries or runtime configurations.
    * KNOWNFOLDERID of the base directory: `FOLDERID_LocalAppData`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\Local\<ApplicationName>\runtime`
        * `with_structure=False`: `C:\Users\<Username>\AppData\Local\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\Local`

### Linux Folders

* `local_data`: Stores application data that doesn't roam with the user. Typically used for storing large datasets or files that are specific to a machine.
    * Base directory: `os.environ.get('XDG_STATE_HOME', os.path.join(os.path.expanduser('~'), '.local', 'state'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.local/state/<ApplicationName>/local/data`
        * `with_structure=False`: `/home/<Username>/.local/state/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.local/state`
* `local_cache`: Used for storing temporary files that enhance application startup and operation. Cache files can be deleted without affecting application functionality.
    * Base directory: `os.environ.get('XDG_CACHE_HOME', os.path.join(os.path.expanduser('~'), '.cache'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.cache/<ApplicationName>/local/cache`
        * `with_structure=False`: `/home/<Username>/.cache/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.cache`
* `local_config`: Stores configuration files. These files usually include settings that are specific to the machine.
    * Base directory: `os.environ.get('XDG_CONFIG_HOME', os.path.join(os.path.expanduser('~'), '.config'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.config/<ApplicationName>/local/config`
        * `with_structure=False`: `/home/<Username>/.config/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.config`
* `local_log`: Used for storing log files generated by the application. Useful for troubleshooting and monitoring application behavior.
    * Base directory: `os.environ.get('XDG_STATE_HOME', os.path.join(os.path.expanduser('~'), '.local', 'state'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.local/state/<ApplicationName>/local/log`
        * `with_structure=False`: `/home/<Username>/.local/state/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.local/state`
* `local_temp`: Intended for temporary files that are needed during the application's execution but not beyond that. These files can be cleared to free up space.
    * Base directory: `os.environ.get('XDG_RUNTIME_DIR', os.path.join(os.path.expanduser('~'), '.tmp'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.tmp/<ApplicationName>/local/temp`
        * `with_structure=False`: `/home/<Username>/.tmp/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.tmp`
* `local_runtime`: Stores files required by the application at runtime. These could include dynamic libraries or runtime configurations.
    * Base directory: `os.environ.get('XDG_RUNTIME_DIR', os.path.join(os.path.expanduser('~'), '.tmp'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.tmp/<ApplicationName>/local/runtime`
        * `with_structure=False`: `/home/<Username>/.tmp/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.tmp`

### macOS Folders

* `local_data`: Stores application data that doesn't roam with the user. Typically used for storing large datasets or files that are specific to a machine.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Application Support/<ApplicationName>/local/data`
        * `with_structure=False`: `/Users/<Username>/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Application Support`
* `local_cache`: Used for storing temporary files that enhance application startup and operation. Cache files can be deleted without affecting application functionality.
    * FileManager.SearchPathDirectory: `cachesDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Caches/<ApplicationName>/local/cache`
        * `with_structure=False`: `/Users/<Username>/Library/Caches/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Caches`
* `local_config`: Stores configuration files. These files usually include settings that are specific to the machine.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Application Support/<ApplicationName>/local/config`
        * `with_structure=False`: `/Users/<Username>/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Application Support`
* `local_log`: Used for storing log files generated by the application. Useful for troubleshooting and monitoring application behavior.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Application Support/<ApplicationName>/local/log`
        * `with_structure=False`: `/Users/<Username>/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Application Support`
* `local_temp`: Intended for temporary files that are needed during the application's execution but not beyond that. These files can be cleared to free up space.
    * FileManager.SearchPathDirectory: `cachesDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Caches/<ApplicationName>/local/temp`
        * `with_structure=False`: `/Users/<Username>/Library/Caches/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Caches`
* `local_runtime`: Stores files required by the application at runtime. These could include dynamic libraries or runtime configurations.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Application Support/<ApplicationName>/local/runtime`
        * `with_structure=False`: `/Users/<Username>/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Application Support`

## Program Data

### Short Description

* `Purpose`: To store application data, settings, and resources that need to be shared across all users on a single computer. Used for global application settings and data.
* `Use Case`: Ideal for system servicess and applications that require storing configuration files, templates, shared databases, or other data that should be accessible system-wide, regardless of the current user.

### Windows Folders

* `program_data`: For data that is shared across all users on the machine. Often used for application data that doesn't contain user-specific settings.
    * KNOWNFOLDERID of the base directory: `FOLDERID_ProgramData`
    * Examples:
        * `with_structure=True`: `C:\ProgramData\<ApplicationName>\data`
        * `with_structure=False`: `C:\ProgramData\<ApplicationName>`
        * `app_name_or_path=None`: `C:\ProgramData`
* `program_cache`: Cache for shared applications and services.
    * KNOWNFOLDERID of the base directory: `FOLDERID_ProgramData`
    * Examples:
        * `with_structure=True`: `C:\ProgramData\<ApplicationName>\cache`
        * `with_structure=False`: `C:\ProgramData\<ApplicationName>`
        * `app_name_or_path=None`: `C:\ProgramData`
* `program_config`: Configuration files for system-wide applications.
    * KNOWNFOLDERID of the base directory: `FOLDERID_ProgramData`
    * Examples:
        * `with_structure=True`: `C:\ProgramData\<ApplicationName>\config`
        * `with_structure=False`: `C:\ProgramData\<ApplicationName>`
        * `app_name_or_path=None`: `C:\ProgramData`
* `program_log`: Log files for system-wide applications.
    * KNOWNFOLDERID of the base directory: `FOLDERID_ProgramData`
    * Examples:
        * `with_structure=True`: `C:\ProgramData\<ApplicationName>\log`
        * `with_structure=False`: `C:\ProgramData\<ApplicationName>`
        * `app_name_or_path=None`: `C:\ProgramData`
* `program_temp`: Temporary files for shared applications.
    * KNOWNFOLDERID of the base directory: `FOLDERID_ProgramData`
    * Examples:
        * `with_structure=True`: `C:\ProgramData\<ApplicationName>\temp`
        * `with_structure=False`: `C:\ProgramData\<ApplicationName>`
        * `app_name_or_path=None`: `C:\ProgramData`
* `program_runtime`: System-wide runtime data like global sockets and named pipes.
    * KNOWNFOLDERID of the base directory: `FOLDERID_ProgramData`
    * Examples:
        * `with_structure=True`: `C:\ProgramData\<ApplicationName>\runtime`
        * `with_structure=False`: `C:\ProgramData\<ApplicationName>`
        * `app_name_or_path=None`: `C:\ProgramData`

### Linux Folders

* `program_data`: For data that is shared across all users on the machine. Often used for application data that doesn't contain user-specific settings.
    * Base directory: `'/var/lib'`
    * Examples:
        * `with_structure=True`: `/var/lib/<ApplicationName>/data`
        * `with_structure=False`: `/var/lib/<ApplicationName>`
        * `app_name_or_path=None`: `/var/lib`
* `program_cache`: Cache for shared applications and services.
    * Base directory: `'/var/cache'`
    * Examples:
        * `with_structure=True`: `/var/cache/<ApplicationName>/cache`
        * `with_structure=False`: `/var/cache/<ApplicationName>`
        * `app_name_or_path=None`: `/var/cache`
* `program_config`: Configuration files for system-wide applications.
    * Base directory: `'/etc'`
    * Examples:
        * `with_structure=True`: `/etc/<ApplicationName>/config`
        * `with_structure=False`: `/etc/<ApplicationName>`
        * `app_name_or_path=None`: `/etc`
* `program_log`: Log files for system-wide applications.
    * Base directory: `'/var/log'`
    * Examples:
        * `with_structure=True`: `/var/log/<ApplicationName>/log`
        * `with_structure=False`: `/var/log/<ApplicationName>`
        * `app_name_or_path=None`: `/var/log`
* `program_temp`: Temporary files for shared applications.
    * Base directory: `'/tmp'`
    * Examples:
        * `with_structure=True`: `/tmp/<ApplicationName>/temp`
        * `with_structure=False`: `/tmp/<ApplicationName>`
        * `app_name_or_path=None`: `/tmp`
* `program_runtime`: System-wide runtime data like global sockets and named pipes.
    * Base directory: `'/var/run'`
    * Examples:
        * `with_structure=True`: `/var/run/<ApplicationName>/runtime`
        * `with_structure=False`: `/var/run/<ApplicationName>`
        * `app_name_or_path=None`: `/var/run`

### macOS Folders

* `program_data`: For data that is shared across all users on the machine. Often used for application data that doesn't contain user-specific settings.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `localDomainMask`
    * Examples:
        * `with_structure=True`: `/Library/Application Support/<ApplicationName>/data`
        * `with_structure=False`: `/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Library/Application Support`
* `program_cache`: Cache for shared applications and services.
    * Note: static path is used as a base directory
    * Base directory: `'/Library/Caches'`
    * Examples:
        * `with_structure=True`: `/Library/Caches/<ApplicationName>/cache`
        * `with_structure=False`: `/Library/Caches/<ApplicationName>`
        * `app_name_or_path=None`: `/Library/Caches`
* `program_config`: Configuration files for system-wide applications.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `localDomainMask`
    * Examples:
        * `with_structure=True`: `/Library/Application Support/<ApplicationName>/config`
        * `with_structure=False`: `/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Library/Application Support`
* `program_log`: Log files for system-wide applications.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `localDomainMask`
    * Examples:
        * `with_structure=True`: `/Library/Application Support/<ApplicationName>/log`
        * `with_structure=False`: `/Library/Application Support/<ApplicationName>`
        * ``app_name_or_path=None`: `/Library/Application Support`
* `program_temp`: Temporary files for shared applications.
    * Note: static path is used as a base directory
    * Base directory: `'/tmp'`
    * Examples:
        * `with_structure=True`: `/tmp/<ApplicationName>/temp`
        * `with_structure=False`: `/tmp/<ApplicationName>`
        * `app_name_or_path=None`: `/tmp`
* `program_runtime`: System-wide runtime data like global sockets and named pipes.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `localDomainMask`
    * Examples:
        * `with_structure=True`: `/Library/Application Support/<ApplicationName>/runtime`
        * `with_structure=False`: `/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Library/Application Support`

## Local App Data Low

### Short Description

* `Purpose`: For storing application data that doesn't require high integrity levels, helping to segregate data based on trust levels and application privileges.
* `Use Case`: Commonly used by web browsers and other applications that execute code or process content from less trusted sources.

### Windows Folders

* `local_low_data`: Low privilege local data storage for sandboxed or security-sensitive applications.
    * KNOWNFOLDERID of the base directory: `FOLDERID_LocalAppDataLow`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\LocalLow\<ApplicationName>\data`
        * `with_structure=False`: `C:\Users\<Username>\AppData\LocalLow\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\LocalLow`
* `local_low_cache`: Similar to local_cache but for applications requiring lower access privileges.
    * KNOWNFOLDERID of the base directory: `FOLDERID_LocalAppDataLow`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\LocalLow\<ApplicationName>\cache`
        * `with_structure=False`: `C:\Users\<Username>\AppData\LocalLow\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\LocalLow`
* `local_low_config`: Configuration for applications with lower privileges.
    * KNOWNFOLDERID of the base directory: `FOLDERID_LocalAppDataLow`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\LocalLow\<ApplicationName>\config`
        * `with_structure=False`: `C:\Users\<Username>\AppData\LocalLow\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\LocalLow`
* `local_low_log`: Logs for low privilege applications.
    * KNOWNFOLDERID of the base directory: `FOLDERID_LocalAppDataLow`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\LocalLow\<ApplicationName>\log`
        * `with_structure=False`: `C:\Users\<Username>\AppData\LocalLow\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\LocalLow`
* `local_low_temp`: Temporary files for applications with lower privileges.
    * KNOWNFOLDERID of the base directory: `FOLDERID_LocalAppDataLow`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\LocalLow\<ApplicationName>\temp`
        * `with_structure=False`: `C:\Users\<Username>\AppData\LocalLow\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\LocalLow`
* `local_low_runtime`: Runtime data for applications with lower privileges.
    * KNOWNFOLDERID of the base directory: `FOLDERID_LocalAppDataLow`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\LocalLow\<ApplicationName>\runtime`
        * `with_structure=False`: `C:\Users\<Username>\AppData\LocalLow\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\LocalLow`

### Linux Folders

* `local_low_data`: Low privilege local data storage for sandboxed or security-sensitive applications.
    * Base directory: `os.environ.get('XDG_STATE_HOME', os.path.join(os.path.expanduser('~'), '.local', 'state'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.local/state/<ApplicationName>/local_low/data`
        * `with_structure=False`: `/home/<Username>/.local/state/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.local/state`
* `local_low_cache`: Similar to local_cache but for applications requiring lower access privileges.
    * Base directory: `os.environ.get('XDG_CACHE_HOME', os.path.join(os.path.expanduser('~'), '.cache'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.cache/<ApplicationName>/local_low/cache`
        * `with_structure=False`: `/home/<Username>/.cache/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.cache`
* `local_low_config`: Configuration for applications with lower privileges.
    * Base directory: `os.environ.get('XDG_CONFIG_HOME', os.path.join(os.path.expanduser('~'), '.config'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.config/<ApplicationName>/local_low/config`
        * `with_structure=False`: `/home/<Username>/.config/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.config`
* `local_low_log`: Logs for low privilege applications.
    * Base directory: `os.environ.get('XDG_STATE_HOME', os.path.join(os.path.expanduser('~'), '.local', 'state'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.local/state/<ApplicationName>/local_low/log`
        * `with_structure=False`: `/home/<Username>/.local/state/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.local/state`
* `local_low_temp`: Temporary files for applications with lower privileges.
    * Base directory: `os.environ.get('XDG_RUNTIME_DIR', os.path.join(os.path.expanduser('~'), '.tmp'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.tmp/<ApplicationName>/local_low/temp`
        * `with_structure=False`: `/home/<Username>/.tmp/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.tmp`
* `local_low_runtime`: Runtime data for applications with lower privileges.
    * Base directory: `os.environ.get('XDG_RUNTIME_DIR', os.path.join(os.path.expanduser('~'), '.tmp'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.tmp/<ApplicationName>/local_low/runtime`
        * `with_structure=False`: `/home/<Username>/.tmp/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.tmp`

### macOS Folders

* `local_low_data`: Low privilege local data storage for sandboxed or security-sensitive applications.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Application Support/<ApplicationName>/local_low/data`
        * `with_structure=False`: `/Users/<Username>/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Application Support`
* `local_low_cache`: Similar to local_cache but for applications requiring lower access privileges.
    * FileManager.SearchPathDirectory: `cachesDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Caches/<ApplicationName>/local_low/cache`
        * `with_structure=False`: `/Users/<Username>/Library/Caches/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Caches`
* `local_low_config`: Configuration for applications with lower privileges.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Application Support/<ApplicationName>/local_low/config`
        * `with_structure=False`: `/Users/<Username>/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Application Support`
* `local_low_log`: Logs for low privilege applications.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Application Support/<ApplicationName>/local_low/log`
        * `with_structure=False`: `/Users/<Username>/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Application Support`
* `local_low_temp`: Temporary files for applications with lower privileges.
    * FileManager.SearchPathDirectory: `cachesDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Caches/<ApplicationName>/local_low/temp`
        * `with_structure=False`: `/Users/<Username>/Library/Caches/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Caches`
* `local_low_runtime`: Runtime data for applications with lower privileges.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Application Support/<ApplicationName>/local_low/runtime`
        * `with_structure=False`: `/Users/<Username>/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Application Support`

## Roaming App Data

### Short Description

* `Purpose`: For storing user-specific application data that should be available across different machines in a network domain.
* `Use Case`: Ideal for applications that need to provide a consistent user experience across multiple workstations, including software configurations, user preferences, and other personal data.

### Windows Folders

* `roaming_data`: Stores user-specific data that should roam with the user profile. Ideal for settings and data that need to be available across different machines.
    * KNOWNFOLDERID of the base directory: `FOLDERID_RoamingAppData`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\Roaming\<ApplicationName>\data`
        * `with_structure=False`: `C:\Users\<Username>\AppData\Roaming\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\Roaming`
* `roaming_cache`: User-specific cache data that could be shared and synced across devices.
    * KNOWNFOLDERID of the base directory: `FOLDERID_RoamingAppData`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\Roaming\<ApplicationName>\cache`
        * `with_structure=False`: `C:\Users\<Username>\AppData\Roaming\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\Roaming`
* `roaming_config`: Configurations that might be synced across a user's devices.
    * KNOWNFOLDERID of the base directory: `FOLDERID_RoamingAppData`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\Roaming\<ApplicationName>\config`
        * `with_structure=False`: `C:\Users\<Username>\AppData\Roaming\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\Roaming`
* `roaming_log`: User-specific logs that might be shared across devices.
    * KNOWNFOLDERID of the base directory: `FOLDERID_RoamingAppData`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\Roaming\<ApplicationName>\log`
        * `with_structure=False`: `C:\Users\<Username>\AppData\Roaming\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\Roaming`
* `roaming_temp`: Temporary user-specific files that might be synced across devices.
    * KNOWNFOLDERID of the base directory: `FOLDERID_RoamingAppData`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\Roaming\<ApplicationName>\temp`
        * `with_structure=False`: `C:\Users\<Username>\AppData\Roaming\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\Roaming`
* `roaming_runtime`: User-specific runtime data that could be synced across devices.
    * KNOWNFOLDERID of the base directory: `FOLDERID_RoamingAppData`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\Roaming\<ApplicationName>\runtime`
        * `with_structure=False`: `C:\Users\<Username>\AppData\Roaming\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\Roaming`

### Linux Folders

* `roaming_data`: Stores user-specific data that should roam with the user profile. Ideal for settings and data that need to be available across different machines.
    * Base directory: `os.environ.get('XDG_STATE_HOME', os.path.join(os.path.expanduser('~'), '.local', 'state'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.local/state/<ApplicationName>/roaming/data`
        * `with_structure=False`: `/home/<Username>/.local/state/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.local/state`
* `roaming_cache`: User-specific cache data that could be shared and synced across devices.
    * Base directory: `os.environ.get('XDG_CACHE_HOME', os.path.join(os.path.expanduser('~'), '.cache'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.cache/<ApplicationName>/roaming/cache`
        * `with_structure=False`: `/home/<Username>/.cache/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.cache`
* `roaming_config`: Configurations that might be synced across a user's devices.
    * Base directory: `os.environ.get('XDG_CONFIG_HOME', os.path.join(os.path.expanduser('~'), '.config'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.config/<ApplicationName>/roaming/config`
        * `with_structure=False`: `/home/<Username>/.config/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.config`
* `roaming_log`: User-specific logs that might be shared across devices.
    * Base directory: `os.environ.get('XDG_STATE_HOME', os.path.join(os.path.expanduser('~'), '.local', 'state'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.local/state/<ApplicationName>/roaming/log`
        * `with_structure=False`: `/home/<Username>/.local/state/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.local/state`
* `roaming_temp`: Temporary user-specific files that might be synced across devices.
    * Base directory: `os.environ.get('XDG_RUNTIME_DIR', os.path.join(os.path.expanduser('~'), '.tmp'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.tmp/<ApplicationName>/roaming/temp`
        * `with_structure=False`: `/home/<Username>/.tmp/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.tmp`
* `roaming_runtime`: User-specific runtime data that could be synced across devices.
    * Base directory: `os.environ.get('XDG_RUNTIME_DIR', os.path.join(os.path.expanduser('~'), '.tmp'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.tmp/<ApplicationName>/roaming/runtime`
        * `with_structure=False`: `/home/<Username>/.tmp/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.tmp`

### macOS Folders

* `roaming_data`: Stores user-specific data that should roam with the user profile. Ideal for settings and data that need to be available across different machines.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Application Support/<ApplicationName>/roaming/data`
        * `with_structure=False`: `/Users/<Username>/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Application Support`
* `roaming_cache`: User-specific cache data that could be shared and synced across devices.
    * FileManager.SearchPathDirectory: `cachesDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Caches/<ApplicationName>/roaming/cache`
        * `with_structure=False`: `/Users/<Username>/Library/Caches/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Caches`
* `roaming_config`: Configurations that might be synced across a user's devices.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Application Support/<ApplicationName>/roaming/config`
        * `with_structure=False`: `/Users/<Username>/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Application Support`
* `roaming_log`: User-specific logs that might be shared across devices.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Application Support/<ApplicationName>/roaming/log`
        * `with_structure=False`: `/Users/<Username>/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Application Support`
* `roaming_temp`: Temporary user-specific files that might be synced across devices.
    * FileManager.SearchPathDirectory: `cachesDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Caches/<ApplicationName>/roaming/temp`
        * `with_structure=False`: `/Users/<Username>/Library/Caches/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Caches`
* `roaming_runtime`: User-specific runtime data that could be synced across devices.
    * FileManager.SearchPathDirectory: `applicationSupportDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Library/Application Support/<ApplicationName>/roaming/runtime`
        * `with_structure=False`: `/Users/<Username>/Library/Application Support/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Library/Application Support`

## Program Files

### Short Description

* `Purpose`: To store executable files and static application data for installed programs. It helps in organizing software installations on a Windows system, ensuring that program files are kept in a dedicated location.
* `Use Case`: Used by software installation processes to place program files and directories. This standard location is recognized by Windows and users for installed applications.

### Windows Folders

* `program_files`:
    * KNOWNFOLDERID of the base directory: `FOLDERID_ProgramFiles`
    * Examples:
        * `with_structure=True`: `C:\Program Files\<ApplicationName>`
        * `with_structure=False`: `C:\Program Files\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Program Files`

### Linux Folders

* `program_files`:
    * Base directory: `'/opt'`
    * Examples:
        * `with_structure=True`: `/opt/<ApplicationName>`
        * `with_structure=False`: `/opt/<ApplicationName>`
        * `app_name_or_path=None`: `/opt`

### macOS Folders

* `program_files`:
    * FileManager.SearchPathDirectory: `allApplicationsDirectory`
    * FileManager.SearchPathDomainMask: `localDomainMask`
    * Examples:
        * `with_structure=True`: `/Applications/<ApplicationName>`
        * `with_structure=False`: `/Applications/<ApplicationName>`
        * `app_name_or_path=None`: `/Applications`

## Program Files Common

### Short Description

* `Purpose`: To house shared libraries, components, and resources that can be used by multiple applications, promoting efficient use of disk space and simplifying updates.
* `Use Case`: Commonly used for storing shared DLLs, data files, and components that provide functionality required by different applications, such as database engines, media codecs, and common utilities.

### Windows Folders

* `program_files_common`:
    * KNOWNFOLDERID of the base directory: `FOLDERID_ProgramFilesCommon`
    * Examples:
        * `with_structure=True`: `C:\Program Files\Common Files\<ApplicationName>`
        * `with_structure=False`: `C:\Program Files\Common Files\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Program Files\Common Files`

### Linux Folders

* `program_files_common`:
    * Base directory: `'/opt'`
    * Examples:
        * `with_structure=True`: `/opt/<ApplicationName>`
        * `with_structure=False`: `/opt/<ApplicationName>`
        * `app_name_or_path=None`: `/opt`

### macOS Folders

* `program_files_common`:
    * FileManager.SearchPathDirectory: `allApplicationsDirectory`
    * FileManager.SearchPathDomainMask: `localDomainMask`
    * Examples:
        * `with_structure=True`: `/Applications/<ApplicationName>`
        * `with_structure=False`: `/Applications/<ApplicationName>`
        * `app_name_or_path=None`: `/Applications`

## User Profile

### Short Description

* `Purpose`: To serve as the root folder for all user-specific data, including personal documents, application settings, and user profile configurations.
* `Use Case`: Essential for operating systems supporting multiple user accounts, ensuring that each user's data and settings are stored separately and securely. Applications can store user-specific data here to ensure it is associated uniquely with the user's profile.
* `Note`: The application name will be prefixed with a leading period on all operating systems.

### Windows Folders

* `user_profile_data`:
    * KNOWNFOLDERID of the base directory: `FOLDERID_Profile`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\.<ApplicationName>`
        * `with_structure=False`: `C:\Users\<Username>\.<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>`

### Linux Folders

* `user_profile_data`:
    * Base directory: `os.path.expanduser('~')`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.<ApplicationName>`
        * `with_structure=False`: `/home/<Username>/.<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>`

### macOS Folders

* `user_profile_data`:
    * FileManager.SearchPathDirectory: `userDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/.<ApplicationName>`
        * `with_structure=False`: `/Users/<Username>/.<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>`

## User Program Files

### Short Description

* `Purpose`: To house user-specific applications and programs, allowing for personalized software installations that do not require administrative privileges for installation or update processes.
* `Use Case`: Particularly useful in environments with multiple users, enabling each user to manage their own set of applications independently of others. This is beneficial for software that users wish to install without altering the system-wide software landscape.

### Windows Folders

* `user_profile_program_files`:
    * KNOWNFOLDERID of the base directory: `FOLDERID_UserProgramFiles`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\Local\Programs\<ApplicationName>`
        * `with_structure=False`: `C:\Users\<Username>\AppData\Local\Programs\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\Local\Programs`

### Linux Folders

* `user_profile_program_files`:
    * Base directory: `os.environ.get('XDG_STATE_HOME', os.path.join(os.path.expanduser('~'), '.local', 'state'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.local/state/<ApplicationName>`
        * `with_structure=False`: `/home/<Username>/.local/state/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.local/state`

### macOS Folders

* `user_profile_program_files`:
    * FileManager.SearchPathDirectory: `applicationDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Applications/<ApplicationName>`
        * `with_structure=False`: `/Users/<Username>/Applications/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Applications`

## User Program Files Common

### Short Description

* `Purpose`: To store shared components, libraries, and resources for applications installed by the current user, promoting efficient use of storage by avoiding duplication and ensuring consistent access to shared resources.
* `Use Case`: Useful for applications that a user installs that need to share common files or components without affecting or requiring access to the system-wide common files directory. This setup is particularly beneficial in multi-user environments where each user has a distinct set of applications and configurations.

### Windows Folders

* `user_profile_program_files_common`:
    * KNOWNFOLDERID of the base directory: `FOLDERID_UserProgramFilesCommon`
    * Examples:
        * `with_structure=True`: `C:\Users\<Username>\AppData\Local\Programs\Common\<ApplicationName>`
        * `with_structure=False`: `C:\Users\<Username>\AppData\Local\Programs\Common\<ApplicationName>`
        * `app_name_or_path=None`: `C:\Users\<Username>\AppData\Local\Programs\Common`

### Linux Folders

* `user_profile_program_files_common`:
    * Base directory: `os.environ.get('XDG_STATE_HOME', os.path.join(os.path.expanduser('~'), '.local', 'state'))`
    * Examples:
        * `with_structure=True`: `/home/<Username>/.local/state/<ApplicationName>`
        * `with_structure=False`: `/home/<Username>/.local/state/<ApplicationName>`
        * `app_name_or_path=None`: `/home/<Username>/.local/state`

### macOS Folders

* `user_profile_program_files_common`:
    * FileManager.SearchPathDirectory: `applicationDirectory`
    * FileManager.SearchPathDomainMask: `userDomainMask`
    * Examples:
        * `with_structure=True`: `/Users/<Username>/Applications/<ApplicationName>`
        * `with_structure=False`: `/Users/<Username>/Applications/<ApplicationName>`
        * `app_name_or_path=None`: `/Users/<Username>/Applications`

## AppDirPath methods

### `__call__(...)`

`def __call__(self, dir_type: AppDirectoryType, app_name_or_path: Optional[DirNameOrPath] = None, with_structure: bool = True, ensure_dir: bool = True) -> str:`

Constructs path of the requestet directory type taking into account provided application name.
* `with_structure`:
    * `False`: determines base directory provided by OS and followed with an application name
    * `True`: determines base directory provided by OS, followed with an application name and completed with a suffixes like 'cache', 'config', 'log', etc.
* `ensure_dir`:
    * `True`: creates directory sequence if does not exists

### `cached(...)`

`def cached(self, dir_type: AppDirectoryType, app_name_or_path: Optional[DirNameOrPath] = None, with_structure: bool = True, ensure_dir: bool = True) -> str:`

Cached version. Much faster in a repetitive requests.

## Global app instances of AppDirPath in Cengal library

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