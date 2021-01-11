import curses
import jfile
import json
import pyotp as otp


class window():
    def __init__(self, x=0, y=0, w=0, h=0):
        count = 0
        ww = curses.COLS
        hh = curses.LINES
        d = {'0': x, '1': y, '2': w, '3': h, }
        if type(x) == float():
            for vars in [x, y, w, h]:
                n = int(vars) * (hh if (count == 0 or count == 2) else ww)
                d[str(count)] = n
                count += 1
            self.x, self.y, self.w, self.h = d['0'], d['1'], d['2'], d['3']
        else:
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
        self.refresh()

    def clean(self):
        lock = 0
        for i in range(self.h - 1):
            if lock == 0:
                lock = 1
                continue
            self.write(i, 1, " "*(self.w - 2))


class totp_win(window):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.json = jfile.get()

    def show(self, string):
        self.clean()
        for i in self.json.items():
            if string in i[0]:
                self.clean()
                self.write(1, 1, f"{i[0]} {self.secret(i[1]['secret'])}")

    def secret(self, code):
        x = otp.TOTP(code)
        return x.now()


class search_win(window):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.json = json.load(open("key.json"))

    def search(self, string):
        self.clean()
        self.write(1, 1, string)
        self.win_totp.show(string)

    def loop(self):
        self.win_totp = totp_win(y=5, x=3, h=3, w=30)
        self.win_totp.build()
        self.win_totp.write(0, 3, "<Result>")
        buffer = ""
        while True:
            key = self.win.getch()
            if key == 9:  # tab to exits
                exit(0)
            if key != 8:  # backspace on my laptop
                try:
                    buffer += self.json[str(key)]
                except:
                    continue
                self.search(buffer)
            else:
                buffer = buffer[:-1]
                self.search(buffer)
