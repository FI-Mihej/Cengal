import os
import sys


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = 'ButenkoMS <gtalk@butenkoms.space>'


def main():
    if sys.platform == 'linux':
        dir_of_the_current_file = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(dir_of_the_current_file)
        parent_dir = os.path.dirname(parent_dir)
        path_to_lib = os.path.join(parent_dir, 'cengal')
        call_result = os.system('export PYTHONPATH=$PYTHONPATH:{}'.format(path_to_lib))
        if path_to_lib not in sys.path:
            sys.path.append(path_to_lib)


if __name__ == '__main__':
    main()
