from curses import wrapper
import exploit, Printer


def main(stdscr):
    stdscr.clear()
    ret = exploit.GadgetFinder(Printer.Printer(stdscr)).find_read_gadget()
    stdscr.addstr(5,0,f"Found load istruction at {hex(ret[0])}: LD {ret[1]} [{ret[2]}]")
    stdscr.getkey()

wrapper(main)