#!/usr/bin/env python3
import re
import snasic_lib.basic_functions.basic_keywords as lang


def grab_command(line):
    return re.split(" ", line, maxsplit=1,
                    flags=re.IGNORECASE)[0].lower()


def run_command(pad, line):
    command = grab_command(line)

    # Don't shadow Python's print function
    if command == "print":
        command = "print_to_screen"
    # Support for the COLOR command to set a background only
    if command == "color,":
        command = "color"
    if "=" in line:
        command = "assign_variable"
    getattr(lang, command)(pad, line)
