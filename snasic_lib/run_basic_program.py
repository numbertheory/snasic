#!/usr/bin/env python3
from snasic_lib.screen import Screen
from snasic_lib.pad import Pad
from snasic_lib.load_file import load_structured_basic_file


def start_program(stdscr, args):
    pad = Pad()
    screen = Screen(stdscr, args)
    basic_script, numbered_lines = load_structured_basic_file(
        args.filename
    )
    while True:
        pad.printpad("hello")
        pad.refresh()
        if pad.pad.getkey():
            break
    return screen
