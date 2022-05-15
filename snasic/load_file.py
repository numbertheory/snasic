#!/usr/bin/env python3


def load_basic_file(filename):
    with open(filename, "r") as f:
        return f.read()
