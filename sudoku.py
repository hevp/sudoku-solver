#!/usr/bin/env python3

import argparse
import sys
from drawer import DrawerFactory
from puzzle import Puzzle
from solver import SolverFactory

def main():
    parser = argparse.ArgumentParser(
                    prog=sys.argv[0],
                    description='Solve any valid sudoku')

    parser.add_argument('filename', type=str)
    parser.add_argument('-d', '--delay', default=0, type=float)
    parser.add_argument('-p', '--progress', action='store_true')
    parser.add_argument('-f', '--fast', action='store_true')

    args = parser.parse_args()

    puzzle = Puzzle(args.filename)
    drawer = DrawerFactory.get("default" if not args.progress else "progress", puzzle=puzzle)
    solver = SolverFactory.get("backtrack", puzzle=puzzle, drawer=drawer, delay=args.delay)

    drawer.draw()
    if not solver.solve(draw=not args.fast):
        print("there is no solution!")

    if args.fast:
        drawer.draw(True)

if __name__ == '__main__':
    main()
