from typing import Dict, List, Tuple

def parse_input(s: str) -> List[List[int]]:
    return [[int(c) for c in l] for l in s.split('\n')]

def in_bound(a: List[List[int]], i: int, j: int) -> bool:
    return i >= 0 and i < len(a) and j >= 0 and j < len(a[0])

def pop_min(Q: Dict[Tuple[int, int], int]) -> Tuple[int, int, int]:
    # TODO: heap optimization
    kk, min_v = None, 2147483647
    for k in Q:
        if Q[k] < min_v:
            min_v = Q[k]
            kk = k
    del Q[kk]
    return kk[0], kk[1], min_v

def solution(a: List[List[int]]) -> int:
    # dijkstra
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    Q = {(0, 0): 0}
    S = {}
    while Q:
        i, j, Qij = pop_min(Q)
        S[(i, j)] = Qij
        for dx, dy in dirs:
            x, y = i + dx, j + dy
            if not in_bound(a, x, y) or (x, y) in S:
                continue
            if (x, y) in Q:
                Q[(x, y)] = min(Q[(x, y)], a[x][y] + Qij)
            else:
                Q[(x, y)] = a[x][y] + Qij
    return S[(len(a) - 1, len(a[0]) - 1)]

def solution1(s: str) -> int:
    return solution(parse_input(s))

def solution2(s: str) -> int:
    a = parse_input(s)
    n = len(a)
    for i in range(1, 5):
        for j in range(n):
            a.append([(x + i - 1) % 9 + 1 for x in a[j]])
    n, m = len(a), len(a[0])
    for i in range(1, 5):
        for j in range(m):
            for k in range(n):
                a[k].append((a[k][j] + i - 1) % 9 + 1)
    return solution(a)
