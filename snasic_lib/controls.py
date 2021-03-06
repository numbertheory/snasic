#!/usr/bin/env python3
import curses


def arrow_keys(screen, y, x, window=[]):
    key = screen.getkey()
    if key == "KEY_LEFT":
        if x > 0:
            x -= 1
    elif key == "KEY_RIGHT":
        if x < (window[1] - 1):
            x += 1
    elif key == "KEY_UP":
        if y > 0:
            y -= 1
    elif key == "KEY_DOWN":
        if y < (window[0] - 1):
            y += 1
    elif key.lower() == "q":
        return None, None
    return y, x


def quit(screen):
    try:
        key = screen.getkey()
    except curses.error:
        key = None
        return key
    if key.lower() == "q":
        exit(0)
    else:
        return key


def scroll(screen, window=[]):
    key = screen.getkey()
    if key == "KEY_UP":
        if screen.scroll_offset > 0:
            screen.scroll_offset -= 1
        return "up"
    elif key == "KEY_DOWN":
        if screen.scroll_offset < (len(screen.content.split('\n')) - 1):
            screen.scroll_offset += 1
        return "down"
    elif key.lower() == "q":
        return None
