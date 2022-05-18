#!/usr/bin/env python3
import re
import time


def print_to_screen(window, line):
    output_string = re.split("print", line, maxsplit=1,
                             flags=re.IGNORECASE)[1]
    quoted_string = " ".join(output_string.split('"')[1::2])
    window.addstr(quoted_string)


def sleep(window, line):
    try:
        sleep_amount = re.split("sleep", line, maxsplit=1,
                                flags=re.IGNORECASE)[1].strip()
        if sleep_amount.isdigit():
            time.sleep(int(sleep_amount))
        else:
            while True:
                if window.getkey():
                    break
    except IndexError:
        print(line)
        raise


def cls(*args):
    args[0].window.erase()
    args[0].cursor_y = 0
    args[0].cursor_x = 0


def locate(window, line):
    try:
        locate_position = re.split("locate", line, maxsplit=1,
                                   flags=re.IGNORECASE)[1].strip().split(",")
        window.cursor_y = int(locate_position[1])
        window.cursor_x = int(locate_position[0])
    except IndexError:
        print(line)
        raise


def color(window, line):
    try:
        text_color = re.split("color", line, maxsplit=1,
                              flags=re.IGNORECASE)[1].strip()
        if text_color.startswith(","):
            new_bg = text_color.replace(", ", "")
            window.active_color = "{},{}".format(window.active_fg, new_bg)
            window.active_bg = new_bg
        elif "," in text_color:
            use_color = [x.strip() for x in text_color.split(",")]
            window.active_color = ",".join(use_color)
            window.active_fg = use_color[0]
            window.active_bg = use_color[1]
        else:
            new_fg = text_color.strip()
            window.active_color = "{},{}".format(new_fg, window.active_bg)
            window.active_fg = new_fg
    except IndexError:
        print(line)
        raise
