import curses


class window():
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = int(x)
        self.y = int(y)
        self.w = int(w)
        self.h = int(h)

    def refresh(self):
        self.win.refresh()

    def build(self):
        self.win = curses.newwin(self.h, self.w, self.y, self.x)
        self.win.border()
        self.refresh()

    def write(self, y, x, string):
        self.win.addstr(y, x, string)

    def clean(self):
        for i in range(self.h):
            self.write(i, 1, " "*(self.w - 2))
