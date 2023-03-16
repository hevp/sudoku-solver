import copy
import math

from functools import reduce

class Puzzle:
    def __init__(self, filename: str):
        self.filename = filename
        self.data = []

        self.load()

    def load(self):
        with open(self.filename, 'r') as f:
            self.data = f.readlines()

        self.data = [int(c) for l in self.data for c in l.strip().split()]
        self.orgdata = copy.deepcopy(self.data)

        self.size = int(math.sqrt(len(self.data)))
        self.blocksize = int(math.sqrt(self.size))

    def in_row(self, value: int, i: int):
        io = i // self.size * self.size
        return value in self.data[io: io + self.size]

    def in_row_y(self, value: int, r: int):
        return value in self.data[r * self.size: r * self.size + self.size]

    def in_col(self, value: int, i: int):
        for c in range(i % self.size, len(self.data), self.size):
            if self.data[c] == value:
                return True
        return False

    def in_col_x(self, value: int, c: int):
        return value in [self.data[i] for i in range(c, len(self.data), self.size)]

    def in_block(self, value: int, i: int):
        io = i // (self.size * self.blocksize) * (self.size * self.blocksize) + (i % self.size) // self.blocksize * self.blocksize
        for y in range(self.blocksize):
            for x in range(self.blocksize):
                if self.data[io + y * self.size + x] == value:
                    return True

        return False

    def in_block_b(self, value: int, b: int):
        i = b // self.blocksize * (self.size * self.blocksize) + b % self.blocksize * self.blocksize
        return value in reduce(lambda x, y: x + self.data[i + (y * self.size): i + (y * self.size) + self.blocksize], range(self.blocksize), [])

    def set_xy(self, value: int, x: int, y: int):
        self.data[y * self.size + x] = value

    def set(self, value: int, i: int):
        self.data[i] = value

    def reset(self):
        self.data = copy.deepcopy(self.orgdata)
