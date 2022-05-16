#!/usr/bin/env python3
import curses
from snasic.screen import Screen
from snasic.controls import arrow_keys


def run(stdscr, args):
    screen = Screen(stdscr, args, content=args.filename)
    x, y = 0, 0
    while True:
        curses.curs_set(False)
        screen.clear()
        screen.refresh()
        screen.printscr(x, y, "X")
        if screen.debug:
            screen.printscr(screen.rows - 1, 0, f"(x, y): {x}, {y}",
                            curses.A_REVERSE)
            screen.refresh()
        screen.refresh()
        x, y = arrow_keys(screen, x, y, window=[screen.rows, screen.cols])
        if (not x) and (not y):
            return screen
