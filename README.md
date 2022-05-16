# snasic

Python BASIC interpreter. There are other ones, this is mine.

## Install

Use python-poetry to install the requirements.

`poetry install`

## Run a BASIC program

`./snasic.py example.bas`

## Snasic command line arguments

- `--list`: List the file instead of running the program
- `--explore`: Launch the cursor explorer program
- `--debug`: Show debug information.
  - Line numbers, scroll offset and filename are shown when listing a program.
  - X, Y coordinates are shown when using `--explore`
  - After successfully running a program, the screen will show the final values python stored. Used for
    debugging snasic itself, not BASIC programs.
- `--help`: show help and exit
- `--version`: show version and quit

## BASIC language commands

- PRINT
  Print to screen
  ```
  PRINT "Hello World"
  ```
