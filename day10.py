from typing import Tuple

def get_result(l: str) -> Tuple[int, str]:
    score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    opening = {')': '(', ']': '[', '}': '{', '>': '<'}
    stack = []
    for c in l:
        if c in '([{<':
            stack.append(c)
        else:
            if stack[-1] != opening[c]:
                return score[c], ''
            else:
                stack.pop()
    return 0, ''.join(stack[::-1])

def solution1(s: str) -> int:
    return sum([get_result(l)[0] for l in s.split('\n')])

def solution2(s: str) -> int:
    results = []
    score = {'(': 1, '[': 2, '{': 3, '<': 4}
    for l in s.split('\n'):
        _, left = get_result(l)
        if left == '':
            continue
        result = 0
        for c in left:
            result *= 5
            result += score[c]
        results.append(result)
    return sorted(results)[len(results) // 2]
