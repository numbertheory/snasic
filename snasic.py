#!/usr/bin/env python3
from snasic_lib.config import Config
from curses import wrapper
from snasic_lib.file_viewer import file_viewer
from snasic_lib.run_basic_program import start_program
from snasic_lib.python_debug import python_debugger
import snasic_lib.explore.explorer as explorer
import toml

args = Config("arguments.yaml")

if (args.version):
    project_info = toml.load("pyproject.toml")
    print("{} - {}".format(
        project_info["tool"]["poetry"]["name"],
        project_info["tool"]["poetry"]["version"]))
    exit(0)


def main(stdscr):
    if (args.list and args.filename):
        screen = file_viewer.load(stdscr, args)
        if screen.debug:
            screen.clear()
            python_debugger(screen, args)

    elif (args.explore):
        screen = explorer.run(stdscr, args)
        if screen.debug:
            python_debugger(screen, args)

    else:
        screen = start_program(stdscr, args)
        if screen.debug:
            python_debugger(screen, args)


if __name__ == '__main__':
    wrapper(main)
