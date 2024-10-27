from cengal.text_processing.text_processing import *


def main():
    from cengal.performance_test_lib import LineType, MeasureTime, measure_time_tl

    first = forbidden_initial_chars[0]
    with measure_time_tl(iterations=1000000) as mt:
        for _ in range(mt.iterations):
            k: bool = first in forbidden_initial_chars

    middle = forbidden_initial_chars[len(forbidden_initial_chars) // 2]
    with measure_time_tl(iterations=1000000) as mt:
        for _ in range(mt.iterations):
            k: bool = middle in forbidden_initial_chars

    with measure_time_tl(iterations=1000000) as mt:
        for _ in range(mt.iterations):
            k: bool = 'a' in forbidden_initial_chars


    with measure_time_tl(iterations=1000000) as mt:
        for _ in range(mt.iterations):
            k: bool = first in forbidden_initial_chars_set

    with measure_time_tl(iterations=1000000) as mt:
        for _ in range(mt.iterations):
            k: bool = middle in forbidden_initial_chars_set

    with measure_time_tl(iterations=1000000) as mt:
        for _ in range(mt.iterations):
            k: bool = 'a' in forbidden_initial_chars_set


    with measure_time_tl(iterations=1000000) as mt:
        for _ in range(mt.iterations):
            k: bool = first in forbidden_initial_chars_list

    with measure_time_tl(iterations=1000000) as mt:
        for _ in range(mt.iterations):
            k: bool = middle in forbidden_initial_chars_list

    with measure_time_tl(iterations=1000000) as mt:
        for _ in range(mt.iterations):
            k: bool = 'a' in forbidden_initial_chars_list


if __name__ == '__main__':
    main()

