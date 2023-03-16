#!/usr/bin/env python3

import sys
from drawer import DrawerFactory
from puzzle import Puzzle
from solver import SolverFactory

def main(args):
    if not len(args):
        print("error: need a file name as argument")
        sys.exit(1)

    p = Puzzle(args[0])

    drawer = DrawerFactory.get("default", puzzle=p)
    solver = SolverFactory.get("backtrack", puzzle=p, drawer=drawer, delay=0.05 if len(args) < 2 else float(args[1]))

    drawer.draw(clear=False)
    if not solver.solve(draw=False):
        print("there is no solution!")

    drawer.draw()

if __name__ == '__main__':
    main(sys.argv[1:])
