from typing import List, Tuple

def parse(s: str) -> Tuple[List[Tuple[int, int]], List[Tuple[str, int]]]:
    section1, section2 = s.split('\n\n')
    dots, folds = [], []
    for l in section1.split('\n'):
        x, y = l.split(',')
        dots.append((int(x), int(y)))
    for l in section2.split('\n'):
        _, _, line = l.split(' ')
        axis, coor = line.split('=')
        folds.append((axis, int(coor)))
    return dots, folds

def reflect(point: Tuple[int, int], line: Tuple[str, int]) -> Tuple[int, int]:
    x, y = point
    axis, coor = line
    if axis == 'x':
        if x > coor:
            x = coor - (x - coor)
        if x == coor:
            return None
    if axis == 'y':
        if y > coor:
            y = coor - (y - coor)
        if y == coor:
            return None
    return x, y

def solution1(s: str) -> int:
    dots, folds = parse(s)
    s = set()
    for dot in dots:
        folded_dot = reflect(dot, folds[0])
        if folded_dot:
            s.add(folded_dot)
    return len(s)

def solution2(s: str):
    dots, folds = parse(s)
    dots = set(dots)
    for fold in folds:
        for dot in list(dots):
            dots.remove(dot)
            folded_dot = reflect(dot, fold)
            if folded_dot:
                dots.add(folded_dot)
    xmax = max(x for x, _ in dots)
    ymax = max(y for _, y in dots)
    for i in range(ymax + 1):
        for j in range(xmax + 1):
            print('#' if (j, i) in dots else ' ', end='')
        print()
