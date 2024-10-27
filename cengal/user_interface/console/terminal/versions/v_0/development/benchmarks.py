from cengal.performance_test_lib import MeasureTimeTraceLine, LineType, MeasureTime, mtimetl, mperformancetl
from cengal.user_interface.console.terminal import sprint, st, fill_current_line, cursor_forward, cursor_up, terminal_width, terminal, \
    set_background_color, BackgroundColor, set_foreground_color, ForegroundColor, erase_screen, erase_line, set_cursor_pos


def main():
    with mperformancetl(0.1, 'Empty line - print()', turn_off_gc=True) as pt:
        while pt():
            print()

    with mperformancetl(0.1, 'Empty line - sprint()', turn_off_gc=True) as pt:
        while pt():
            sprint()


if '__main__' == __name__:
    main()
