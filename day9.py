from typing import List

def parse(s: str) -> List[List[int]]:
    return [[int(c) for c in l] for l in s.split('\n')]

def in_bound(h: List[List[int]], i: int, j: int) -> bool:
    return i >= 0 and i < len(h) and j >= 0 and j < len(h[0])

def is_low_point(h: List[List[int]], i: int, j: int) -> bool:
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in d:
        x, y = i + dx, j + dy
        if not in_bound(h, x, y):
            continue
        if h[i][j] >= h[x][y]:
            return False
    return True

def solution1(s: str) -> int:
    h = parse(s)
    ans = 0
    for i in range(len(h)):
        for j in range(len(h[0])):
            if is_low_point(h, i, j):
                ans += h[i][j] + 1
    return ans

def solution2(s: str) -> int:
    h = parse(s)
    sizes = []
    def dfs(i: int, j: int):
        h[i][j] = '_'
        sizes[-1] += 1
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in d:
            x, y = i + dx, j + dy
            if in_bound(h, x, y) and h[x][y] not in ['_', 9]:
                dfs(x, y)
    for i in range(len(h)):
        for j in range(len(h[0])):
            if h[i][j] not in ['_', 9]:
                sizes.append(0)
                dfs(i, j)
    print('\n'.join([''.join([str(x) for x in l]) for l in h]))
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]
