#!/usr/bin/env python3
from snasic.config import Config
from curses import wrapper
from snasic.controls import arrow_keys
from snasic.screen import Screen
from snasic.load_file import load_basic_file
import curses

args = Config("arguments.yaml")


def main(stdscr):
    x, y = 0, 0
    screen = Screen(stdscr)
    if (args.list and args.filename):
        file_text = load_basic_file(args.filename)
        while True:
            screen.clear()
            screen.load_scrolling_content(file_text)
            screen.refresh()
            screen.quit()

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
