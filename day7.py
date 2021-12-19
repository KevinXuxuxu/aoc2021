def solution1(s: str) -> int:
    a = [int(n) for n in s.split(',')]
    median = sorted(a)[len(a)//2]
    return sum([abs(n - median) for n in a])

def _feul_cost2(dist: int) -> int:
    return (1 + dist) * dist / 2

def solution2(s: str) -> int:
    a = [int(n) for n in s.split(',')]
    mean = round(sum(a) / len(a))
    return sum(_feul_cost2(abs(n - mean + 1)) for n in a) # why +1 ?
