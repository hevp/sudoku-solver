import time

from drawer import Drawer
from puzzle import Puzzle

class Solver:
    def __init__(self, puzzle: Puzzle, drawer: Drawer, delay: float = 0.05):
        self.puzzle = puzzle
        self.drawer = drawer
        self.delay = delay
        self.draw = True

    def solve(self, draw: bool = True):
        self.draw = draw
        return self.run()


class BacktrackerSolver(Solver):
    def run(self, i: int = 0):
        while self.puzzle.get(i):
            i += 1
            if i >= self.puzzle.size ** 2:
                return True

        for n in range(1, self.puzzle.size + 1):
            if not self.puzzle.in_row(n, i) and not self.puzzle.in_col(n, i) and not self.puzzle.in_block(n, i):
                self.puzzle.set(n, i)
                if self.draw:
                    self.drawer.update(i)
                    time.sleep(self.delay)
                if self.run(i):
                    return True
                self.puzzle.set(0, i)
                #if self.draw:
                    #self.drawer.update(i)

        return False


class SolverFactory:
    @staticmethod
    def get(name: str, **kwargs):
        match name:
            case "backtrack":
                return BacktrackerSolver(**kwargs)
            case _:
                return BacktrackerSolver(**kwargs)
