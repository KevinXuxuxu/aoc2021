from typing import List

def in_bound(a: List[List[int]], i: int, j: int) -> bool:
    return i >= 0 and i < len(a) and j >= 0 and j < len(a[0])

def dfs(a: List[List[int]], i: int, j: int):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    for dx, dy in dirs:
        x, y = i + dx, j + dy
        if not in_bound(a, x, y) or a[x][y] in [0, -1]:
            continue
        a[x][y] += 1
        if a[x][y] == 10:
            a[x][y] = 0
            dfs(a, x, y)

def step(a: List[List[int]]) -> int:
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] += 1
            if a[i][j] == 10:
                a[i][j] = -1
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == -1:
                a[i][j] = 0
                dfs(a, i, j)
    cnt = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 0:
                cnt += 1
    return cnt

def print_a(a: List[List[int]]):
    for l in a:
        print(''.join([str(i) for i in l]))
    print()


def solution1(s: str, steps: int = 100) -> int:
    a = [[int(c) for c in l] for l in s.split('\n')]
    ans = 0
    for _ in range(steps):
        ans += step(a)
        # print_a(a)
    return ans

def solution2(s: str) -> int:
    a = [[int(c) for c in l] for l in s.split('\n')]
    n = len(a) * len(a[0])
    i = 1
    while step(a) != n:
        i += 1
    return i
