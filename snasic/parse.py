#!/usr/bin/env python3
import re


def run_command(screen, line):
    if line.lower().startswith("print"):
        try:
            output_string = re.split("print", line, maxsplit=1,
                                     flags=re.IGNORECASE)[1]
            quoted_string = " ".join(output_string.split('"')[1::2])
            screen.printscr(screen.cursor_y, screen.cursor_x, quoted_string)
        except IndexError:
            print(line)
            raise
        screen.cursor_y += 1
