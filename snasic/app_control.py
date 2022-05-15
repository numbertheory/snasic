#!/usr/bin/env python3
import curses


def snasic_break(stdscr):
    try:
        key = stdscr.getkey()
    except curses.error:
        key = None
        return key
    if key.lower() == "q":
        exit(0)
    else:
        return key
