# snasic

Python BASIC interpreter. There are other ones, this is mine.

## Install

Use python-poetry to install the requirements.

`poetry install`

## Run a BASIC program

`./snasic.py example.bas`

## Snasic command line arguments

- `--list`: List the file instead of running the program. Use the `Q` key to quit.
- `--explore`: Launch the cursor explorer program. Use the `Q` key to quit.
- `--debug`: Show debug information.
  - Line numbers, scroll offset and filename are shown when listing a program. Python debugger is run after quitting.
  - X, Y coordinates are shown when using `--explore`. Python debugger is run after quitting.
  - After successfully running a program, the screen will show the final values python stored. Used for debugging snasic itself, not BASIC programs.
- `--help`: show help and exit
- `--version`: show version and quit

## BASIC language commands

- PRINT
  Print to screen
  ```
  PRINT "Hello World"
  ```
- SLEEP
  Pause the execution of a program for a number of seconds. Use SLEEP by itself to
  wait for a key to be pressed.
  ```
  SLEEP 10
  SLEEP
  ```
- CLS
  Clears the screen, and resets the cursor to 0, 0 (top-left of the screen). `CLS` is not necessary for the first command, as all output is in a [Python curses](https://docs.python.org/3/library/curses.html) window to prevent breaking the user's terminal.
  ```
  CLS
  ```
 - COLOR [fg, bg]
   Sets the color for the text for the next PRINT commands. See table for color options. Use a comma immediately after the color keyword to set the background color only. Add 16 to the normal color value for foreground text color to set the text to blink. Blinking background is not available.
   ```
   COLOR 1, 2 (set foreground and background colors)
   COLOR 2 (set foreground color only)
   COLOR, 3 (set background color only)
   ```
   | Color Value  | Color   | Blink Value |
   | -------------| ------- | ----------- |
   | 0            | BLACK   | 16          |
   | 1            | RED     | 17          |
   | 2            | GREEN   | 18          |
   | 3            | YELLOW  | 19          |
   | 4            | BLUE    | 20          |
   | 5            | MAGENTA | 21          |
   | 6            | CYAN    | 22          |
   | 7            | WHITE   | 23          |
   | 8            | GREY    | 24          |

  - LOCATE [row, col]
  Set the cursor to an arbitrary row and col on the screen. Indexed to 0. The line
  prints at the position, and then next line prints on the next row, at the 0 column
  position.

  ```
  LOCATE 0, 20
  PRINT "Hello World"
  PRINT "Another Line"
  ```

  - Variable assignment
  Assign variables as strings or numbers
  ```
  a = "j"
  b = 12
  PRINT "b$, a$"
  ```
