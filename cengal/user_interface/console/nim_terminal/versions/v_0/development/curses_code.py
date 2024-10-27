import curses

def main(stdscr):
    # Clear screen
    # stdscr.clear()
    
    stdscr.addstr("Press 'Ctrl+G' to exit or use arrow keys.\n")
    stdscr.addstr("Press any key to see its code.\n")
    stdscr.refresh()

    while True:
        key: int = stdscr.getch()
        key_bin: bytes = key.to_bytes(4, 'little')

        if key == 7:  # Ctrl+G is ASCII value 7
            stdscr.addstr("Ctrl+G pressed, exiting...\n")
            stdscr.refresh()
            break
        elif key == curses.KEY_UP:
            stdscr.addstr(f"Up arrow pressed: {key} (ASCII {chr(key)}) (BYTES {key_bin})\n")
        elif key == curses.KEY_DOWN:
            stdscr.addstr(f"Down arrow pressed: {key} (ASCII {chr(key)}) (BYTES {key_bin})\n")
        elif key == curses.KEY_LEFT:
            stdscr.addstr(f"Left arrow pressed: {key} (ASCII {chr(key)}) (BYTES {key_bin})\n")
        elif key == curses.KEY_RIGHT:
            stdscr.addstr(f"Right arrow pressed: {key} (ASCII {chr(key)}) (BYTES {key_bin})\n")
        elif key == ord('S') - ord('A') + 1:  # Ctrl+S is ASCII value 19
            stdscr.addstr(f"Ctrl+S pressed: {key} (ASCII {chr(key)}) (BYTES {key_bin})\n")
        else:
            stdscr.addstr(f"Key pressed: {key} (ASCII {chr(key)}) (BYTES {key_bin})\n")
        
        print('-----')

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
