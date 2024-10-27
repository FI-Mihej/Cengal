import cProfile

prof_file_name = 'cengal_import_test__profiling.prof'
# cProfile.run('from cengal_import_test import importing_time', 'cengal_import_test__profiling.prof')
# cProfile.run('from cengal_import_test import importing_time', prof_file_name, sort='cumulative')
cProfile.run('from cengal_import_test import importing_time', prof_file_name)

import pstats
from pstats import SortKey
p = pstats.Stats(prof_file_name)
# p.strip_dirs().sort_stats(-1).print_stats()
p.sort_stats('cumulative').print_stats()
# p.sort_stats('tottime').print_stats()
