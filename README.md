# Sudok solver
Straightforward sudoku solver using different strategies and drawing algorithms.

## Extendability
You can easily extend the code with your own solving strategies. Simply create a class derived from the `Solver` class and make sure the `SolverFactory` can find it based on a unique string. Then you can use that string in the main program.

Same holds for the drawing strategy in the console (or any other output). Inherit the `Drawer` class and make sure the `DrawerFactory` can find it based on again a unique string.

## Usage
Enter the following command:

```sh
./sudoku.py <filename>
```

An optional second argument sets the delay per iteration (e.g. 0.01 seconds)
