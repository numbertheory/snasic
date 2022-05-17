#!/usr/bin/env python3
import curses


class Pad:
    def __init__(self):
        self.pad = curses.newpad(100, 100)

    def printpad(self, content):
        self.pad.addstr(0, 0, content)
        self.refresh()

    def refresh(self):
        self.pad.refresh(0, 0, 0, 0, 10, 10)

    def clear(self):
        pass
