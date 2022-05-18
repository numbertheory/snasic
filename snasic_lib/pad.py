#!/usr/bin/env python3
import curses


class Pad:
    def __init__(self, screen):
        self.screen = screen
        self.pad = curses.newwin(screen.rows, screen.cols)
        self.pad_x = 0
        self.pad_y = 0
        self.cursor_x = 0
        self.cursor_y = 0
        self.scroll_amt = 0
        self.pad.scrollok(True)
        self.pad.idlok(True)

    def addstr(self, content):
        self.pad.addstr(self.cursor_x, 0, "{}".format(content))
        self.pad.refresh()
        if self.screen.rows - 1 > self.cursor_x:
            self.cursor_x += 1
        else:
            self.pad.scroll(1)



    def refresh(self, ulp=[0, 0], ulw=[0, 0], lrw=[None, None]):
        if not lrw[0]:
            lrw[0] = self.screen.rows
        if not lrw[1]:
            lrw[1] = self.screen.cols
        # A pad contains a window, which contains the text
        # ulp - upper-left coordinate of the pad area (relative to screen)
        # ulw - upper-left coordinate of the window area (relative to the pad)
        # lrw - lower-right coordinate of the window area (relative to the pad)
        self.pad.refresh(ulp[0], ulp[1], ulw[0], ulw[1], lrw[0], lrw[1])


    def clear(self):
        pass
