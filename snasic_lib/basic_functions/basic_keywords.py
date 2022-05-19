#!/usr/bin/env python3
import re
import time


def print_to_screen(window, line):
    output_string = re.split("print", line, maxsplit=1,
                             flags=re.IGNORECASE)[1]
    quoted_string = " ".join(output_string.split('"')[1::2])
    if "$" in quoted_string:
        vars = quoted_string.split(" ")
        full_string = list()
        for word in vars:
            if "$" in word:
                full_string.append(
                    window.basic_variables.get(word.replace("$", ""), ""))
            else:
                full_string.append(word)
        full_string = " ".join(full_string)
    else:
        full_string = quoted_string
    window.addstr(full_string)


def assign_variable(window, line):
    value = re.split("=", line, maxsplit=1,
                     flags=re.IGNORECASE)
    key = value[0]
    if value[1].isdigit():
        var_val = int(value[1])
    else:
        var_val = value[1]
    window.basic_variables[key.strip()] = " ".join(var_val.strip().split('"')[1::2])


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
