#!/usr/bin/env python3
import curses
from snasic.controls import quit
from snasic.load_file import load_basic_file


class Screen:
    def __init__(self, stdscr, args, content=None):
        self.screen = stdscr
        self.end_message = "Program Ended - Press any key to exit."
        self.last_key_pressed = None
        self.rows, self.cols = self.screen.getmaxyx()
        self.visible = [''] * self.rows
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
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

    def printscr(self, y, x, content, format=None):
        try:
            if format:
                self.screen.addstr(y, x, content, format)
            else:
                self.screen.addstr(y, x, content, curses.color_pair(1))
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
