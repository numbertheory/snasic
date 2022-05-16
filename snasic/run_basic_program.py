#!/usr/bin/env python3
import curses
from snasic.screen import Screen
from snasic.load_file import load_structured_basic_file
from snasic.parse import run_command


def start_program(stdscr, args):
    curses.endwin()
    screen = Screen(stdscr, args)
    screen.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    screen.screen.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
    basic_script, numbered_lines = load_structured_basic_file(
        args.filename
    )
    while True:
        for line in basic_script:
            if((line["command"].strip() != "") and
               (line["command"] is not None)):
                run_command(screen, line["command"])
                screen.refresh()
        screen.printscr(screen.rows - 1, 0,
                        screen.end_message.ljust(screen.cols),
                        curses.A_REVERSE)
        screen.refresh()
        if screen.getkey():
            screen.last_key_pressed = screen.getkey()
            break
    return screen
