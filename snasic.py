#!/usr/bin/env python3
from snasic.config import Config
from curses import wrapper
from snasic.controls import arrow_keys, scroll
from snasic.screen import Screen
from snasic.load_file import load_structured_basic_file
from snasic.parse import run_command
import curses
import toml

args = Config("arguments.yaml")

if (args.version):
    project_info = toml.load("pyproject.toml")
    print("{} - {}".format(
        project_info["tool"]["poetry"]["name"],
        project_info["tool"]["poetry"]["version"]))
    exit(0)


def main(stdscr):
    x, y = 0, 0
    screen = Screen(stdscr, args, content=args.filename)
    if (args.list and args.filename):
        while True:
            screen.clear()
            screen.load_scrolling_content()
            scroll(screen)
            screen.refresh()

    elif (args.explore):
        while True:
            curses.curs_set(False)
            screen.clear()
            screen.refresh()
            screen.printscr(x, y, "X")
            screen.refresh()
            if screen.debug:
                screen.printscr(screen.rows - 1, 0, f"(x, y): {x},{y}",
                                curses.A_REVERSE)
                screen.refresh()
            screen.refresh()
            x, y = arrow_keys(screen, x, y, window=[screen.rows, screen.cols])

    else:
        curses.endwin()
        screen = Screen(stdscr, args)
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
                            "Program Ended - Press any key to exit.",
                            curses.A_REVERSE)
            screen.refresh()
            if screen.getkey():
                break


if __name__ == '__main__':
    wrapper(main)
