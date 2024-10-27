from cengal.os.process.memory_info import get_process_tree_memory_info
from cengal.user_interface.console.progress_meter import ProgressMeter, ProgressOutType
from cengal.os.process.ensure_environment import *
from cengal.os.process.prepare_cmd_line import *

from os import getpid

print('Started')
pm: ProgressMeter = ProgressMeter(0.1, 'processes')
print(get_process_tree_memory_info(getpid(), progress_callback=lambda _: pm()))
print()

pm.reset()
print(get_process_tree_memory_info(2472, progress_callback=lambda _: pm()))  # browser
print('Done')
