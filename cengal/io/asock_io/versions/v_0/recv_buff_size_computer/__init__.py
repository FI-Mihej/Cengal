try:
    from .recv_buff_size_computer__cython import *
except ImportError:
    from .recv_buff_size_computer__cpython import *

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = 'ButenkoMS <gtalk@butenkoms.space>'