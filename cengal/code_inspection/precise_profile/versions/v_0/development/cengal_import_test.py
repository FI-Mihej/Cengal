from time import perf_counter as time_perf_counter
start_time = time_perf_counter()

# from cengal.time_management.cpu_clock_cycles import perf_counter
# from cengal.system import *
# import numpy as np
# from numpy import ndarray
from cengal.hardware.memory.shared_memory import *
# import rich

end_time = time_perf_counter()
importing_time = end_time - start_time
print(f'Imports: {importing_time:.6f} seconds')
raise RuntimeError('End of the test')


# from time import perf_counter
# start_time = perf_counter()
# from cengal.performance_test_lib import LineType, MeasureTime, measure_time_tl
# from cengal.introspection.inspect import pcen, cen, pifr, pifrl, intro_func_repr_limited
# from cengal.hardware.memory.barriers import full_memory_barrier
# from cengal.code_inspection.auto_line_tracer import tl, tr, t, alt, LineType, OutputFields, AutoLineTracer
# from cengal.user_interface.console.terminal import sprint, st, fill_current_line, cursor_forward, cursor_up, terminal_width, terminal, \
#     set_background_color, BackgroundColor, set_foreground_color, ForegroundColor, erase_screen, erase_line, set_cursor_pos
# from cengal.hardware.memory.shared_memory import *
# from cengal.parallel_execution.asyncio.ashared_memory_manager import *

# from multiprocessing import Process, Manager
# from os.path import basename
# from dataclasses import dataclass
# from enum import IntEnum

# # import numpy as np
# from typing import Union, List, Callable
# end_time = perf_counter()
# importing_time = end_time - start_time
# print(f'Imports: {importing_time:.6f} seconds')
