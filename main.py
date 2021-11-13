from curses import wrapper
import re
from sys import byteorder
import tqdm
import exploit, Printer

def dump_mem(memreader,fname = "out.bin"):
    with open(fname,"wb") as f:
        for i in tqdm.tqdm(range(0x08000000,0x08100000,4)):
            f.write(memreader.read_mem(i).to_bytes(length=4,byteorder='little'))
        f.close()

def main(stdscr):
    ret = None#(0x8000832,"R3","R3")
    gf = exploit.GadgetFinder(Printer.Printer(stdscr))

    if not ret:
        stdscr.clear()
        ret = gf.find_read_gadget()
        stdscr.addstr(5,0,f"Found load istruction at {hex(ret[0])}: LD {ret[1]} [{ret[2]}]")
        stdscr.getkey()

    mr = exploit.MemReader(ret,gf)
    stdscr.addstr(6,0,f"\n\rMemory at location 0x080004c6: {mr.read_mem(0x080004c6).to_bytes(length=4,byteorder='little')}")
    dump_mem(mr)
    stdscr.getkey()

wrapper(main)