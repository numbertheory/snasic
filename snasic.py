#!/usr/bin/env python3
from snasic.config import Config
from curses import wrapper
from snasic.arrow_keys import controls
from snasic.app_control import snasic_break
from snasic.screen import printscr
import curses

args = Config("arguments.yaml")


def main(stdscr):
    x, y = 0, 0
    if (args.list and args.filename):
        rows, cols = stdscr.getmaxyx()
        while True:
            stdscr.clear()
            stdscr.refresh()
            snasic_break(stdscr)

    elif (args.filename):
        while True:
            curses.curs_set(False)
            stdscr.clear()
            stdscr.refresh()
            printscr(x, y, stdscr, "X")
            stdscr.refresh()
            x, y = controls(stdscr, x, y, window=[rows, cols])


if __name__ == '__main__':
    wrapper(main)
