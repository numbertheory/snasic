#!/usr/bin/env python3
import curses
from snasic.controls import quit
from snasic.load_file import load_basic_file


class Screen:
    def __init__(self, stdscr, args, content=None):
        self.screen = stdscr
        self.rows, self.cols = self.screen.getmaxyx()
        self.visible = [''] * self.rows
        self.args = args
        self.debug = self.args.debug
        self.file_list = self.args.list
        self.row_limit = self.set_row_limit()
        if self.args.list:
            self.content = load_basic_file(content)
        else:
            self.content = None

    def printscr(self, y, x, stdscr, content):
        try:
            self.screen.addstr(y, x, content)
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

    def getmaxyx(self):
        return self.screen.getmaxyx()

    def load_scrolling_content(self):
        lines = self.content.split('\n')
        self.row_limit = self.set_row_limit()
        for i, line in enumerate(lines):
            if i < self.row_limit:
                try:
                    if self.debug:
                        line_number = str(i).zfill(3)
                        self.screen.addstr(i, 0, f"{line_number} " + line)
                    else:
                        self.screen.addstr(i, 0, line)

                except curses.error:
                    pass

    def getkey(self):
        return self.screen.getkey()

    def quit(self):
        return quit(self.screen)
