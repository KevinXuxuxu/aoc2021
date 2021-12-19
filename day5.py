from typing import Tuple

def _get_point(s: str) -> Tuple[int, int]:
    return [int(p) for p in s.split(',')]

def _get_direction(a: int, b: int) -> int:
    return (b - a) // abs(b - a)

def solution(s: str, with_diag: bool = False) -> int:
    d = [[0] * 1000 for _ in range(1000)]
    for l in s.split('\n'):
        a, b = l.split(' -> ')
        x1, y1 = _get_point(a)
        x2, y2 = _get_point(b)
        if max(max(x1, x2), max(y1, y2)) >= 1000:
            print(x1, y1, x2, y2)
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2)+1):
                d[x1][i] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)+1):
                d[i][y1] += 1
        elif with_diag:
            dx, dy = _get_direction(x1, x2), _get_direction(y1, y2)
            x, y = x1, y1
            while x != x2:
                d[x][y] += 1
                x += dx
                y += dy
            d[x][y] += 1
    ans = 0
    for i in range(1000):
        for j in range(1000):
            if d[i][j] > 1:
                ans += 1
    return ans
