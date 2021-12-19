import re

class Board:

    def __init__(self, s: str):
        self.sum = 0
        self.cols = [0] * 5
        self.rows = [0] * 5
        self.d = {}
        for i, l in enumerate(s.split('\n')):
            for j, n in enumerate(re.split(' +', l.strip())):
                v = int(n)
                self.sum += v
                self.rows[i] += v
                self.cols[j] += v
                self.d[v] = (i, j)

    def mark(self, v: int) -> bool:
        if v not in self.d:
            return False
        i, j = self.d[v]
        self.rows[i] -= v
        self.cols[j] -= v
        self.sum -= v
        del self.d[v]
        if self.rows[i] * self.cols[j] == 0:
            return True
        return False

def solution1(s: str) -> int:
    parts = s.split('\n\n')
    series = [int(n) for n in parts[0].split(',')]
    boards = [Board(part) for part in parts[1:]]
    for v in series:
        for b in boards:
            if b.mark(v):
                return b.sum * v

def solution2(s: str) -> int:
    parts = s.split('\n\n')
    series = [int(n) for n in parts[0].split(',')]
    boards = [Board(part) for part in parts[1:]]
    ans = None
    for v in series:
        for i in range(len(boards)):
            b = boards[i]
            if b != None:
                if b.mark(v):
                    ans = b.sum * v
                    boards[i] = None
    return ans

