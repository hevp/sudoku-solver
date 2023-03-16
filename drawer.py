import sys

from puzzle import Puzzle

class Drawer:
    def __init__(self, puzzle: Puzzle):
        self.puzzle = puzzle
        self.lastdraw = self.puzzle.size ** 2

    def draw(self, clear: bool = True):
        if clear:
            for i in range(self.puzzle.size):
                sys.stdout.write("\x1b[1A\x1b[2K")

        for i in range(self.puzzle.size * self.puzzle.size):
            col = '\033[31m' if self.puzzle.data[i] != self.puzzle.orgdata[i] else '\033[0m'
            e = '\n' if i % self.puzzle.size == (self.puzzle.size - 1) else ' '
            sys.stdout.write(f"{col}{self.puzzle.data[i]:>2}\033[0m{e}")

    def update(self, i: int = 0):
        self.draw()

class SimpleDrawer(Drawer):
    def update(self, i: int = 0):
        pass

class CoordinatedDrawer(Drawer):
    def update(self, i: int = 0):
        d = i - self.lastdraw

        if d != 0:
            dx = (i % self.puzzle.size) - (self.lastdraw % self.puzzle.size)
            dy = (i // self.puzzle.size) - (self.lastdraw // self.puzzle.size)
            #sys.stdout.write(f"{i} {self.lastdraw} {d} {dx} {dy}\n")

            if i == 16:
                sys.exit()
            # move cursor up / down
            if dy != 0:
                sys.stdout.write(f"\033[{abs(dy)}{'F' if dy < 0 else 'E'}")
            # move cursor left / right
            if dx != 0:
                sys.stdout.write(f"\033[{abs(dx * 3)}{'D' if dx < 0 else 'C'}")

        col = '\033[31m' if self.puzzle.data[i] != self.puzzle.orgdata[i] else '\033[0m'
        sys.stdout.write(f"{col}{self.puzzle.data[i]:>2}\033[0m")

        self.lastdraw = i


class DrawerFactory:
    @staticmethod
    def get(name: str, **kwargs):
        match name:
            case "coordinated":
                return CoordinatedDrawer(**kwargs)
            case "simple":
                return SimpleDrawer(**kwargs)
            case _:
                return Drawer(**kwargs)
