"""
compile_time_py_definitions.go

"""
# python wrapper for package cengal/_examples/ex_golang/versions/v_0/compilable/compile_time_py_definitions within overall package greeter
# This is what you import to use the package.
# File is generated by gopy. Do not edit.
# gopy build -output=compiled -vm=C:\Dev\Compilers\Python39\python.exe ./src ./compile_time_py_definitions

# the following is required to enable dlopen to open the _go.so file
import os,sys,inspect,collections
try:
	import collections.abc as _collections_abc
except ImportError:
	_collections_abc = collections

cwd = os.getcwd()
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(currentdir)
from . import _greeter
from . import go

os.chdir(cwd)

# to use this code in your end-user python file, import it as follows:
# from greeter import compile_time_py_definitions
# and then refer to everything using compile_time_py_definitions. prefix
# packages imported by this package listed below:




# ---- Types ---


#---- Enums from Go (collections of consts with same type) ---


#---- Constants from Go: Python can only ask that you please don't change these! ---
ApiEndpointDoc = "URL: https://api.production.com; Path: \\usr\\bin"
GOD_CENGAL_VERSION_MAJOR = 4
GOD_CENGAL_VERSION_MAJOR_STR = "4"
GOD_CENGAL_VERSION_MICRO = 1
GOD_CENGAL_VERSION_MICRO_STR = "1"
GOD_CENGAL_VERSION_MINOR = 4
GOD_CENGAL_VERSION_MINOR_STR = "4"
GOD_CENGAL_VERSION_STR = "4.4.1"
GOD_COMPILER_NAME = ""
GOD_COMPILER_STRING = ""
GOD_COMPILER_TYPE = "unknown"
GOD_CPU_ARCH = "X86_64"
GOD_CPU_ARCH_RAW_STRING = "AMD64"
GOD_CPU_BITS = 64
GOD_IS_ARM = 0
GOD_IS_ARM_BOOL = False
GOD_IS_BUILDING_FOR_PYODIDE = 0
GOD_IS_BUILDING_FOR_PYODIDE_BOOL = False
GOD_IS_INSIDE_OR_FOR_WEB_BROWSER = 0
GOD_IS_INSIDE_OR_FOR_WEB_BROWSER_BOOL = False
GOD_IS_RUNNING_IN_EMSCRIPTEN = 0
GOD_IS_RUNNING_IN_EMSCRIPTEN_BOOL = False
GOD_IS_RUNNING_IN_PYCHARM = 0
GOD_IS_RUNNING_IN_PYCHARM_BOOL = False
GOD_IS_RUNNING_IN_PYODIDE = 0
GOD_IS_RUNNING_IN_PYODIDE_BOOL = False
GOD_IS_RUNNING_IN_WASI = 0
GOD_IS_RUNNING_IN_WASI_BOOL = False
GOD_IS_X86 = 1
GOD_IS_X86_BOOL = True
GOD_KIVY_PLATFORM = "unknown"
GOD_KIVY_TARGET_PLATFORM = "unknown"
GOD_OS_API_TYPE = "nt"
GOD_OS_TYPE = "Windows"
GOD_PYTHON_IMPLEMENTATION = "CPython"
GOD_PYTHON_VERSION_MAJOR = 3
GOD_PYTHON_VERSION_MAJOR_STR = "3"
GOD_PYTHON_VERSION_MICRO = 13
GOD_PYTHON_VERSION_MICRO_STR = "13"
GOD_PYTHON_VERSION_MINOR = 9
GOD_PYTHON_VERSION_MINOR_STR = "9"
GOD_PYTHON_VERSION_STR = "3.9.13"
GOD_RAW_OS_PLATFORM = "win32"
GOD_UNAME_MACHINE = "AMD64"
GOD_UNAME_SYSNAME = "Windows"


# ---- Global Variables: can only use functions to access ---


# ---- Interfaces ---


# ---- Structs ---


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---


# ---- Functions ---


