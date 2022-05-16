#!/usr/bin/env python3
from snasic.screen import Screen
from snasic.controls import scroll


def load(stdscr, args):
    screen = Screen(stdscr, args, content=args.filename)
    while True:
        screen.clear()
        screen.load_scrolling_content()
        screen.refresh()
        scroller = scroll(screen)
        if not scroller:
            break
    screen.content = ""
    return screen
