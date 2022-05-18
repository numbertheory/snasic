#!/usr/bin/env python3
import curses
from snasic_lib.basic_functions import color_palette


class Window:
    def __init__(self, screen):
        self.screen = screen
        self.window = curses.newwin(screen.rows + 1, screen.cols)
        curses.curs_set(0)
        self.cursor_x = 0
        self.cursor_y = 0
        self.scroll_amt = 0
        self.window.scrollok(True)
        self.window.idlok(True)
        self.active_bg = "0"
        self.active_fg = "7"
        self.active_color = "7,0"
        self.end_message = "Program Ended - Press any key to exit."
        self.colors = color_palette.initialize_color_pairs()

    def addstr(self, content, format=curses.A_NORMAL):
        if int(self.active_fg) >= 16:
            self.active_fg = str(int(self.active_fg) - 16)
            self.active_color = "{},{}".format(self.active_fg, self.active_bg)
            pair = self.colors.get(self.active_color)
            color = curses.color_pair(pair)
            format = curses.A_BLINK
        else:
            pair = self.colors.get(self.active_color)
            color = curses.color_pair(pair)

        self.window.addstr(self.cursor_x, self.cursor_y,
                           content, color | format)
        self.window.refresh()
        if self.screen.rows - 1 > self.cursor_x:
            self.cursor_x += 1
            self.cursor_y = 0
        else:
            self.window.scroll(1)
            self.cursor_y = 0

    def end_program_message(self):
        self.active_bg = "0"
        self.active_fg = "2"
        self.active_color = "2,0"
        self.window.addstr(self.screen.rows, 0,
                           self.end_message.ljust(self.screen.cols),
                           curses.A_REVERSE)

    def clear(self):
        self.screen.clear()
        self.window.refresh()

    def getkey(self):
        return self.screen.getkey()
