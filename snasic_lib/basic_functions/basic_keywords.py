#!/usr/bin/env python3
import re
import time


def print_to_screen(pad, line):
    output_string = re.split("print", line, maxsplit=1,
                             flags=re.IGNORECASE)[1]
    quoted_string = " ".join(output_string.split('"')[1::2])
    pad.addstr(quoted_string)



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


def color(screen, line):
    try:
        text_color = re.split("color", line, maxsplit=1,
                              flags=re.IGNORECASE)[1].strip()
        if text_color.startswith(","):
            new_bg = text_color.replace(", ", "")
            screen.active_color = "{},{}".format(screen.active_fg, new_bg)
            screen.active_bg = new_bg
        elif "," in text_color:
            use_color = [x.strip() for x in text_color.split(",")]
            screen.active_color = ",".join(use_color)
            screen.active_fg = use_color[0]
            screen.active_bg = use_color[1]
        else:
            new_fg = text_color.strip()
            screen.active_color = "{},{}".format(new_fg, screen.active_bg)
            screen.active_fg = new_fg
    except IndexError:
        print(line)
        raise
