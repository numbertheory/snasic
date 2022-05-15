#!/usr/bin/env python3
import curses


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
        self.screen.addstr(0, 0, content)

    def getkey(self):
        return self.screen.getkey()
