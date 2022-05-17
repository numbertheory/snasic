#!/usr/bin/env python3
from snasic_lib.screen import Screen
from snasic_lib.pad import Pad


def start_program(stdscr, args):
    pad = Pad()
    screen = Screen(stdscr, args)
    while True:
        pad.printpad("hello")
        pad.refresh()
        if pad.pad.getkey():
            break
    return screen
