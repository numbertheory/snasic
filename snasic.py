#!/usr/bin/env python3
from snasic.config import Config
from curses import wrapper
from snasic.arrow_keys import controls
from snasic.app_control import snasic_break
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
            snasic_break(stdscr)

    elif (args.filename):
        while True:
            curses.curs_set(False)
            screen.clear()
            screen.refresh()
            screen.printscr(x, y, stdscr, "X")
            screen.refresh()
            x, y = controls(screen, x, y, window=[screen.rows, screen.cols])


if __name__ == '__main__':
    wrapper(main)
