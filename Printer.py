class Printer:
    def __init__(self,stdscr) -> None:
        self.curline = 0
        self.stdscr = stdscr
    
    def spinning_cursor(self):
        cursor = "|/-\\"
        i = 0
        while True:
            yield cursor[i]
            i = (i + 1) % len(cursor)

    def print_append(self,msg):
        self.curline += 1
        self.print_on_line(self.curline,msg)

    def print(self,msg):
        self.print_on_line(self.curline,0,msg)

    def print_on_line(self,linum,msg):
        self.stdscr.move(linum,0)
        self.stdscr.clrtoeol()
        self.stdscr.addstr(linum,0,msg)
        self.stdscr.refresh()

        if linum > self.curline:
            self.curline = linum
