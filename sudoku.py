#!/usr/bin/env python3

import sys
from drawer import DrawerFactory
from puzzle import Puzzle
from solver import SolverFactory

def main(args):
    if not len(args):
        print("error: need a file name as argument")
        sys.exit(1)

    puzzle = Puzzle(args[0])
    drawer = DrawerFactory.get("default", puzzle=puzzle)
    solver = SolverFactory.get("backtrack", puzzle=puzzle, drawer=drawer, delay=0.05 if len(args) < 2 else float(args[1]))

    drawer.draw()
    if not solver.solve():
        print("there is no solution!")

if __name__ == '__main__':
    main(sys.argv[1:])
