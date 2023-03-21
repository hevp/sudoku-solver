# Sudoku solver
Straightforward sudoku puzzle solver using different strategies and drawing algorithms.

## Extendability
You can easily extend the code with your own solving strategies. Simply create a class derived from the `Solver` class and make sure the `SolverFactory` can find it based on a unique string. Then you can use that string in the main program.

Same holds for the drawing strategy in the console (or any other output). Inherit the `Drawer` class and make sure the `DrawerFactory` can find it based on again a unique string.

## Usage
Enter the following command:

```sh
$ ./sudoku.py <filename> [<options>]
```

The following options are available:

```sh
$ ./sudoku.py -h
usage: ./sudoku.py [-h] [-d DELAY] [-p] [-f] filename

Solve any valid sudoku

positional arguments:
  filename              File name of the puzzle

options:
  -h, --help            show this help message and exit
  -d DELAY, --delay DELAY
                        Time delay per iteration
  -p, --progress        Show progress bar instead of puzzle
  -f, --fast            Don't draw intermediate steps
```
