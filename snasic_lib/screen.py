#!/usr/bin/env python3
import curses
from snasic_lib.controls import quit
from snasic_lib.load_file import load_basic_file
from snasic_lib.basic_functions import color_palette


class Screen:
    def __init__(self, stdscr, args, content=None):
        self.screen = stdscr
        self.end_message = "Program Ended - Press any key to exit."
        self.rows, self.cols = self.screen.getmaxyx()
        self.args = args
        self.debug = self.args.debug
        self.filename = content
        self.row_limit = self.set_row_limit()
        self.scroll_offset = 0
        if self.args.list:
            self.content = load_basic_file(content)
        else:
            self.content = None
        self.cursor_x = 0
        self.cursor_y = 0
        self.colors = color_palette.initialize_color_pairs()
        self.active_color = "7,0"
        self.active_bg = "0"
        self.active_fg = "7"

    def printscr(self, y, x, content, format=None):
        if int(self.active_fg) >= 16:
            self.active_fg = str(int(self.active_fg) - 16)
            self.active_color = "{},{}".format(self.active_fg, self.active_bg)
            pair = self.colors.get(self.active_color)
            color = curses.color_pair(pair)
            format = curses.A_BLINK
        else:
            pair = self.colors.get(self.active_color)
            color = curses.color_pair(pair)

        try:
            if format:
                self.screen.addstr(y, x, content, color | format)
            else:
                pair = self.colors.get(self.active_color)
                self.screen.addstr(y, x, content, color)
        except curses.error:
            pass

    def set_row_limit(self):
        self.rows, self.cols = self.screen.getmaxyx()
        if self.debug:
            return self.rows - 1
        else:
            return self.rows

    def clear(self):
        self.screen.clear()

    def refresh(self):
        self.rows, self.cols = self.screen.getmaxyx()
        if self.content:
            self.load_scrolling_content()
            self.screen.refresh()
        self.screen.refresh()

    def getmaxyx(self):
        return self.screen.getmaxyx()

    def load_scrolling_content(self):
        lines = self.content.split('\n')
        self.row_limit = self.set_row_limit()
        if len(lines[self.scroll_offset:]) < self.rows:
            for i in range(0, self.rows - len(lines[self.scroll_offset:])):
                lines.append("")
        for i, line in enumerate(lines[self.scroll_offset:]):
            if i < self.row_limit:
                try:
                    if self.debug:
                        line_number = str(i+self.scroll_offset+1).zfill(3)
                        self.screen.addstr(i, 0,  f"{line_number}",
                                           curses.A_DIM)
                        self.screen.addstr(i, 4, line)
                    else:
                        self.screen.addstr(i, 0, line)

                except curses.error:
                    pass
        if self.debug:
            debug_text = f"Scr:{self.scroll_offset} " \
                         f"File: {self.filename}".ljust(self.cols)
            self.printscr(self.rows - 1, 0,
                          debug_text,
                          curses.A_REVERSE)

    def getkey(self):
        return self.screen.getkey()

    def quit(self):
        return quit(self.screen)

    def use_default_colors(self):
        curses.use_default_colors()
