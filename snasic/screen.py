#!/usr/bin/env python3
import curses


def printscr(y, x, stdscr, content):
    try:
        stdscr.addstr(y, x, content)
    except curses.error:
        pass
