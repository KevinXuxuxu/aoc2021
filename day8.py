from typing import Dict, List

def parse_and_sort(s: str) -> List[str]:
    return [''.join(sorted(x)) for x in s.split(' ')]

def solve_mapping(code: List[str]) -> Dict[str, int]:
    d = {}
    b = {}
    for c in code:
        if len(c) == 2:
            d[c], b[1] = 1, c
        elif len(c) == 3:
            d[c], b[7] = 7, c
        elif len(c) == 4:
            d[c], b[4] = 4, c
        elif len(c) == 7:
            d[c], b[8] = 8, c
    for c in code:
        if c in d:
            continue
        if len(c) == 6:
            if len(set(c) - set(b[4]).union(set(b[7]))) == 1:
                d[c], b[9] = 9, c
            else:
                if len(set(b[1]) - set(c)) == 1:
                    d[c], b[6] = 6, c
                else:
                    d[c], b[0] = 0, c
        elif len(c) == 5:
            if len(set(c) - set(b[7])) == 2:
                d[c], b[3] = 3, c
            elif len(set(c) - set(b[4]).union(set(b[7]))) == 1:
                d[c], b[5] = 5, c
            else:
                d[c], b[2] = 2, c
    return d

def solution1(s: str) -> int:
    ans = 0
    for l in s.split('\n'):
        code, nums = l.split(' | ')
        for num in nums.split(' '):
            if len(num) in [2, 3, 4, 7]:
                ans += 1
    return ans

def solution2(s: str) -> int:
    ans = 0
    for l in s.split('\n'):
        code, nums = l.split(' | ')
        code = parse_and_sort(code)
        nums = parse_and_sort(nums)
        d = solve_mapping(code)
        ans += int(''.join([str(d[n]) for n in nums]))
    return ans
