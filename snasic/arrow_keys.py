#!/usr/bin/env python3

def controls(screen, y, x, window=[]):
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
        exit(0)
    return y, x
