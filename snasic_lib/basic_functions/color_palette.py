#!/usr/bin/env python3
import curses


def initialize_color_pairs():
    pairs = 1
    lookup_table = dict()
    for fg in range(0, 9):
        for bg in range(0, 9):
            curses.init_pair(pairs, fg, bg)
            lookup_table[f"{fg},{bg}"] = pairs
            pairs += 1
    return lookup_table
