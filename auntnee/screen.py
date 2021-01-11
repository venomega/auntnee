import win


def scr(stdscr):
    search = win.search_win(x=3, y=1, h=3, w=30)
    search.build()
    search.write(0, 2, "<SEARCH>")
    search.loop()
