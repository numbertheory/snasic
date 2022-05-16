#! /usr/bin/env python3

def python_debugger(screen, args):
    while True:
        screen.clear()
        screen.printscr(1, 1, "Welcome to Python!")
        screen.screen.border()
        screen.printscr(2, 1, f"self.rows = {screen.rows}")
        screen.printscr(3, 1, f"self.cols = {screen.cols}")
        screen.printscr(4, 1, f"self.visible = {len(screen.visible)} items"
                              f" - {set(screen.visible)}")

        screen.refresh()
        if screen.getkey():
            break
