#!/usr/bin/env python3
import curses
from snasic.controls import quit


class Screen:
    def __init__(self, stdscr):
        self.screen = stdscr
        self.rows, self.cols = self.screen.getmaxyx()
        self.visible = [''] * self.rows

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

    def load_scrolling_content(self, content):
        lines = content.split('\n')
        for i, line in enumerate(lines):
            self.screen.addstr(i, 0, line)

    def getkey(self):
        return self.screen.getkey()

    def quit(self):
        return quit(self.screen)
