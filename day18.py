import copy
from typing import List, Union

def is_int(n: Union[int, List]) -> bool:
    return type(n) == int

def mag(n: Union[int, List]) -> int:
    if type(n) == int:
        return n
    return 3 * mag(n[0]) + 2 * mag(n[1])

def scan(n: List) -> bool:
    prev = [None, None]
    add_right = [None]
    done = [False, False]
    def explode(n: List, d: int):
        for i in range(2):
            if done[0] and add_right[0] is None:
                return
            if is_int(n[i]):
                if add_right[0] is not None:
                    n[i] += add_right[0]
                    add_right[0] = None
                prev[0] = n
                prev[1] = i
            else:
                if d == 4 and add_right[0] is None:
                    if prev[0]:
                        prev[0][prev[1]] += n[i][0]
                    add_right[0] = n[i][1]
                    n[i] = 0
                    done[0] = True
                else:
                    explode(n[i], d+1)
    explode(n, 1)
    if done[0]:
        return True
    def split(n: List):
        for i in range(2):
            if done[1]:
                return
            if is_int(n[i]):
                if n[i] >= 10:
                    n[i] = [n[i]//2, n[i] - n[i]//2]
                    done[1] = True
            else:
                split(n[i])
    split(n)
    return done[0] or done[1]

def reduce(n: List):
    changed = True
    while changed:
        changed = scan(n)

def add(n: List[int], m: List[int]) -> List[int]:
    v = [copy.deepcopy(n), copy.deepcopy(m)]
    reduce(v)
    return v

def solution1(s: str) -> int:
    nums = [eval(l) for l in s.split('\n')]
    ans = nums[0]
    for n in nums[1:]:
        ans = add(ans, n)
    return mag(ans)

def solution2(s: str) -> int:
    nums = [eval(l) for l in s.split('\n')]
    ans = 0
    x = None
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                ans = max(ans, mag(add(nums[i], nums[j])))
    return ans
