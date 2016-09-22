# About Cengal

**Cengal** is a Python library that consists of various Python helping modules for everyday use. 

It holds modules for multiprocessing, async IO, code flow control, folder traversal, app settings management, 
console output, etc. 

It is made for [CPython 2/3 and PyPy 2/3; Linux, Win32 and OS X]

## Size of the Cengal library

How much of your time you can save if you'll use Cengal?

That much:

```

-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                          81           2050           3005           8760
Cython                           2            120             69            435
Markdown                         2             49              0            236
-------------------------------------------------------------------------------
SUM:                            85           2219           3074           9431
-------------------------------------------------------------------------------
TOTAL:                                                                    14724
-------------------------------------------------------------------------------

```
Counted with [cloc](https://github.com/AlDanial/cloc) util.

# Installation

1. Clone repo or download and unpack archive.
2. Add root folder (that contains this Readme) to PYTHONPATH environment variable.

Now you can import modules from it:
* `import check_is_in_pycharm`
* `import code_inspection`
* `from code_flow_control import ResultExistence`
* etc.

# Some of the Modules (most interesting)

* **IO**:
    * **"simple_network"** (will be renamed to **"ASockIO"**) - high-level, fast, powerful and robust IO library. 
    * **"net_io"** - simple async TCP server/client. It's much closer to raw sockets and not isolates "connection" objects from the user's code.
* **Multiprocessing**:
    * **"multiprocess"** - you can run workers (separate processes or threads) and stream data pieces to them. Exceptions will be transmitted to the calling code and thrown on an appropriate processing result obtaining.
* **Code Flow Control**:
    * **"code_flow_control/smart_chain"** - allows you to easily implement code execution chain (for separate functions or for code blocks) with complex rules. It can be characterized as a kind of a Chain Monad implementation. See "Tools" and [Bensbach](https://github.com/FI-Mihej/Bensbach) compiler for examples.
* **App Settings**:
    * **"file_settings_manager"** - simple (and easy to use) app settings manager for settings inside of the User_Folder with settings template support. Cross platform (Win32, Linux). See "Tools" for examples.
* **File System**:
    * **For Win32 (long unicode path support)**:
        * **"file_system/win_fs"** - injectable/uninstallable in runtime cross-Python (for whole program and currently used libs) support for Win32 long unicode path.
    * **"file_system"** - dir tools (easy to use directory traversal and other) and file tools. Cross platform. Can work properly with Win32 long unicode path (see "file_system/win_fs" module).
* **Modules management**:
    * **"modules_management"** - implements cross-version (for both Python 2 and 3, and for PyPy) module reloading. Also works useful from the Python console.
* **Testing**:
    * **"testing_lib"** - you can chose exact test to run (or all test one after another) from the console menu. Useful, for example, when each test is a complex app/script and you need to test how one app/script communicates with another.
    * **"performance_test_lib"** - test performance of the separate functions or code blocks.
* **Data Containers**:
    * **"data_containers"** - various smart data containers.
* **PIP Automation**:
    * **"bulk_pip_actions"** - automatically install all modules you need with rules for different OS (Win32/Linux/OsX) and Python versions (2/3) and implementations (CPython/PyPy).
* **Environment Check**:
    * **"check_is_in_pycharm"** - will check is code running under PyCharm (with full Unicode In-Out and unix-like coloring support).

## Examples

Some examples lies inside the module. Some - inside the **"setup_scripts/Tests"** dir.

# Tools

There are some applications in Cengal (will be moved from it into separate modules in one of the next refactoring processes).
They are lies in **"various_tools"** directory.

All tools will memorise last used inputs and configurations inside User Dir folder (cross platform)

* **"all_tools_runner.py"** is an entry point for all tools. It's useful both with and without compiling all tools to the single executable.
* **Search Through Files' Content**:
    * **"find_in_files"** - fast search through files' content. Run with "help" or "h" or "?" command line parameter for detailed help. Found line can be opened in the text editor (should be set in the "<User Dir>/.PythonLibs Settings/Various Tools/known external editors". It will be created after first run of this tool.).
        * Use "s " prefix for text search. For example (s Some Unicode string request);
        * Use "se " prefix for Unicode string with Escape characters. For example (se Some line\nSome new line);
        * and "h "" - for the HEX values. For example (h 4F 94 AD 00 FF);
    * **"replace_in_files"** - fast content replacing.
* **File Search**:
    * **"find_files"** - will find all files that contain given text in their names.
    * **"find_all_file_extensions_in_folder"** - will find all file extensions in given folder.
    * **"list_simlinks"** - will find all symlinks in the given folder.
* **Win32 Dir Copy With Long Unicode File Names**:
    * **"copy_dir"** - made to copy large dirs with long path under Win32 ("Explorer"© will fail to do this. Core Python libs are also helpless in this task.). Able to recognize symlinks.
* **Source Code Metrics**:
    * **"count_loc_py"** - will count "Lines Of Code" (without commented and empty/spaced lines) in given folder for files with given extensions.
* **Various**:
    * **"unit_converter"** - basic converter (only between inches and centimeters currently).

# License

Copyright © 2016 ButenkoMS. All rights reserved.

Licensed under the Apache License, Version 2.0.
