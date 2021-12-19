from typing import Dict, List
from collections import defaultdict

def parse_graph(s: str) -> Dict[str, List[str]]:
    d = defaultdict(list)
    for l in s.split('\n'):
        a, b = l.split('-')
        d[a].append(b)
        d[b].append(a)
    return d

def solution1(s: str) -> int:
    d = parse_graph(s)
    # print(d)
    cnt = [0]
    def dfs(cave: str, path: List[str]):
        if cave == 'end':
            cnt[0] += 1
            # print(path)
            return
        for nxt in d[cave]:
            if nxt.islower() and nxt in path:
                continue
            dfs(nxt, path + [nxt])
    dfs('start', ['start'])
    return cnt[0]

def check_path(path: List[str], cave: str) -> bool:
    if cave.isupper() or cave not in path:
        return True
    if cave == 'start':
        return False
    s = set()
    for c in path:
        if c.islower():
            if c in s:
                return False
            s.add(c)
    return True

def solution2(s: str) -> int:
    d = parse_graph(s)
    # print(d)
    cnt = [0]
    def dfs(cave: str, path: List[str]):
        if cave == 'end':
            cnt[0] += 1
            # print(path)
            return
        for nxt in d[cave]:
            if check_path(path, nxt):
                dfs(nxt, path + [nxt])
    dfs('start', ['start'])
    return cnt[0]
