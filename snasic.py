#!/usr/bin/env python3
from snasic.config import Config
from curses import wrapper
from snasic.controls import arrow_keys, scroll
from snasic.screen import Screen
import curses

args = Config("arguments.yaml")


def main(stdscr):
    x, y = 0, 0
    screen = Screen(stdscr, args, content=args.filename)
    if (args.list and args.filename):
        while True:
            screen.clear()
            screen.load_scrolling_content()
            scroll(screen)
            screen.refresh()

    elif (args.filename):
        while True:
            curses.curs_set(False)
            screen.clear()
            screen.refresh()
            screen.printscr(x, y, stdscr, "X")
            screen.refresh()
            x, y = arrow_keys(screen, x, y, window=[screen.rows, screen.cols])


if __name__ == '__main__':
    wrapper(main)
