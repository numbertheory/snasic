#! /usr/bin/env python3

def python_debugger(screen, args, window=None):
    while True:
        screen.clear()
        screen.screen.border()
        screen.active_color = "7,0"
        screen.active_bg = "0"
        screen.active_fg = "7"
        screen.printscr(1, 1, "Welcome to Python!")
        screen.printscr(2, 1, f"self.rows = {screen.rows}")
        screen.printscr(3, 1, f"self.cols = {screen.cols}")
        if window:
            screen.printscr(4, 1, f"window vars: {window.basic_variables}")

        screen.refresh()
        if screen.getkey():
            break
