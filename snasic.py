#!/usr/bin/env python3
from snasic.config import Config
from curses import wrapper
import curses
import time

args = Config("arguments.yaml")


def key_controls(stdscr, y, x):
    key = stdscr.getkey()
    if key == "KEY_LEFT":
        x -= 1
    elif key == "KEY_RIGHT":
        x += 1
    elif key == "KEY_UP":
        y -= 1
    elif key == "KEY_DOWN":
        y += 1
    elif key == "Q":
        exit(0)
    return y, x


def main(stdscr):
    x, y = 0, 0
    while True:
        stdscr.clear()
        stdscr.addstr(x, y, "X")
        stdscr.refresh()
        x, y = key_controls(stdscr, x, y)


if __name__ == '__main__':
    wrapper(main)
