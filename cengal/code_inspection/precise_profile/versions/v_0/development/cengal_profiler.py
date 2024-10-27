from cengal.code_inspection.precise_profile import Profile, SortKey

with Profile('from cengal_import_test import importing_time') as p:
    p.print_stats()


# from cengal.code_inspection.precise_profile import profile, precise_pstats, SortKey

# with precise_pstats():
#     profile('from cengal_import_test import importing_time').print_stats()


from cengal.file_system.file_manager import remove_file_after_usage

with remove_file_after_usage('cengal_import_test__profiling.prof') as prof_file_name:
    import cProfile
    from cengal.code_flow_control.exception_to_warning import exception_to_warning

    # cProfile.run('from cengal_import_test import importing_time', 'cengal_import_test__profiling.prof')
    # cProfile.run('from cengal_import_test import importing_time', prof_file_name, sort='cumulative')
    with exception_to_warning():
        cProfile.run('from cengal_import_test import importing_time', prof_file_name)

    import pstats
    from pstats import SortKey
    p = pstats.Stats(prof_file_name)
    # p.strip_dirs().sort_stats(-1).print_stats()
    p.sort_stats('cumulative').print_stats()
    # p.sort_stats('tottime').print_stats()
