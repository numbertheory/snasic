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
