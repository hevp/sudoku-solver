import copy
import math

from functools import reduce

class Puzzle:
    def __init__(self, filename: str):
        self.filename = filename
        self.data = {}

        self.load()

    def load(self):
        with open(self.filename, 'r') as f:
            self.rawdata = f.readlines()

        self.data['rows'] = [[int(c) for c in l.strip().split()] for l in self.rawdata]
        self.size = len(self.data['rows'])
        self.blocksize = int(math.sqrt(self.size))

        # extract columns and blocks
        self.data['cols'] = [[r[i] for r in self.data['rows']] for i in range(self.size)]
        self.data['blocks'] = []
        for b in range(self.size):
            xo, yo = b % self.blocksize * self.blocksize, b // self.blocksize * self.blocksize
            self.data['blocks'].append(reduce(lambda x, y: x + self.data['rows'][yo + y][xo:xo + self.blocksize], range(self.blocksize), []))

        self.orgdata = copy.deepcopy(self.data)

    def in_row(self, value: int, i: int):
        return value in self.data['rows'][i // self.size]

    def in_row_y(self, value: int, r: int):
        return value in self.data['rows'][r]

    def in_col(self, value: int, i: int):
        return value in self.data['cols'][i % self.size]

    def in_col_x(self, value: int, c: int):
        return value in self.data['cols'][c]

    def in_block(self, value: int, i: int):
        return value in self.data['blocks'][i // (self.size * self.blocksize) * self.blocksize + (i % self.size) // self.blocksize]

    def in_block_b(self, value: int, b: int):
        return value in self.data['blocks'][b]

    def set_xy(self, value: int, x: int, y: int):
        self.data['rows'][y][x] = value
        self.data['cols'][x][y] = value
        b, i = y // self.blocksize + x // self.blocksize, x % self.blocksize + y % self.blocksize
        self.data['blocks'][b][i] = value

    def set(self, value: int, i: int):
        x, y = i % self.size, i // self.size
        self.data['rows'][y][x] = value
        self.data['cols'][x][y] = value
        b = i // (self.size * self.blocksize) * self.blocksize + (i % self.size) // self.blocksize
        o = (i // self.size) % self.blocksize * self.blocksize + i % self.blocksize
        self.data['blocks'][b][o] = value

    def get_xy(self, x: int, y: int):
        return self.data['rows'][y][x]

    def get(self, i: int):
        return self.data['rows'][i // self.size][i % self.size]

    def changed(self, i: int):
        return self.data['rows'][i // self.size][i % self.size] != self.orgdata['rows'][i // self.size][i % self.size]

    def reset(self):
        self.data = copy.deepcopy(self.orgdata)
