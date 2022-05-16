#!/usr/bin/env python3
import re
import time


def print_to_screen(screen, line):
    try:
        output_string = re.split("print", line, maxsplit=1,
                                 flags=re.IGNORECASE)[1]
        quoted_string = " ".join(output_string.split('"')[1::2])
        screen.printscr(screen.cursor_y, screen.cursor_x, quoted_string)
    except IndexError:
        print(line)
        raise
    screen.cursor_y += 1


def sleep(screen, line):
    try:
        sleep_amount = re.split("sleep", line, maxsplit=1,
                                flags=re.IGNORECASE)[1].strip()
        if sleep_amount.isdigit():
            time.sleep(int(sleep_amount))
        else:
            while True:
                if screen.getkey():
                    break
    except IndexError:
        print(line)
        raise


def cls(*args):
    args[0].clear()
    args[0].cursor_y = 0
    args[0].cursor_x = 0
