#!/usr/bin/env python3


def load_basic_file(filename):
    if not filename:
        return None
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found. Use ./snasic.py --help for more info"


def load_structured_basic_file(filename):
    if not filename:
        return None
    try:
        with open(filename, "r") as f:
            data = f.read()

        lines = data.split('\n')
        output = list()
        numbered_lines = dict()
        for line in lines:
            if line.split(" ")[0].isdigit():
                separated_line = line.split(" ")
                line_number = separated_line[0]
                if len(separated_line) > 1:
                    command = " ".join(separated_line[1:])
                else:
                    command = ""
                numbered_lines[int(line_number)] = command
            else:
                line_number = None
                command = line
            output.append({"line_number": line_number,
                           "command": command.strip()})
        return output, numbered_lines
    except FileNotFoundError:
        return "File not found. Use ./snasic.py --help for more info"
