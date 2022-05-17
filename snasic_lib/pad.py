#!/usr/bin/env python3
import curses


class Pad:
    def __init__(self):
        self.pad = curses.newpad(100, 100)

    def printpad(self, content):
        self.pad.addstr(0, 0, content)
        self.refresh()

    def refresh(self, ulp=(0, 0), ulw=(0, 0), lrw=(10, 10)):
        # A pad contains a window, which contains the text
        # ulp - upper-left coordinate of the pad area (relative to screen)
        # ulw - upper-left coordinate of the window area (relative to the pad)
        # lrw - lower-right coordinate of the window area (relative to the pad)
        self.pad.refresh(ulp[0], ulp[1], ulw[0], ulw[1], lrw[0], lrw[1])

    def clear(self):
        pass
