#!/usr/bin/env python3
import curses
from snasic_lib.screen import Screen
from snasic_lib.load_file import load_structured_basic_file
from snasic_lib.parse import run_command


def start_program(stdscr, args):
    curses.endwin()
    screen = Screen(stdscr, args)
    screen.use_default_colors()
    basic_script, numbered_lines = load_structured_basic_file(
        args.filename
    )
    while True:
        for line in basic_script:
            if((line["command"].strip() != "") and
               (line["command"] is not None)):
                run_command(screen, line["command"])
                screen.refresh()
        screen.active_color = "7,0"
        screen.active_bg = "7"
        screen.avtive_fg = "0"
        screen.printscr(screen.rows - 1, 0,
                        screen.end_message.ljust(screen.cols),
                        curses.A_REVERSE)
        if screen.getkey():
            break
    return screen