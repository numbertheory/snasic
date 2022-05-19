#!/usr/bin/env python3
from snasic_lib.screen import Screen
from snasic_lib.window import Window
from snasic_lib.load_file import load_structured_basic_file
from snasic_lib.parse import run_command


def start_program(stdscr, args):
    screen = Screen(stdscr, args)
    window = Window(screen)
    basic_script, numbered_lines = load_structured_basic_file(
        args.filename
    )
    while True:
        for line in basic_script:
            if((line["command"].strip() != "") and
               (line["command"] is not None)):
                run_command(window, line["command"])
        window.end_program_message()
        if window.window.getkey():
            break
    return screen, window
