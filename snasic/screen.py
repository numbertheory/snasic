#!/usr/bin/env python3
import curses
from snasic.controls import quit
from snasic.load_file import load_basic_file


class Screen:
    def __init__(self, stdscr, debug, content=None):
        self.screen = stdscr
        self.rows, self.cols = self.screen.getmaxyx()
        self.visible = [''] * self.rows
        self.debug = debug
        if self.debug:
            self.row_limit = self.rows - 3
        else:
            self.row_limit = self.rows
        if content:
            self.content = load_basic_file(content)
        else:
            self.content = None

    def printscr(self, y, x, stdscr, content):
        try:
            self.screen.addstr(y, x, content)
        except curses.error:
            pass

    def clear(self):
        self.screen.clear()

    def refresh(self):
        self.rows, self.cols = self.screen.getmaxyx()
        self.screen.refresh()

    def getmaxyx(self):
        return self.screen.getmaxyx()

    def load_scrolling_content(self):
        self.refresh()
        lines = self.content.split('\n')
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
