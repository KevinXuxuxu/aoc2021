import math
from typing import Tuple

def solution1(x_range: Tuple[int, int], y_range: Tuple[int, int]) -> int:
    x_min, x_max = x_range
    y_min, y_max = y_range
    v_y = -y_min - 1
    return int(v_y * (v_y + 1) / 2)
    # t = 2 * v_y + 2
    # (v + (v - t + 1))t/2 >= x_min
    # v_x = math.ceil(x_min/t + (t-1)/2)

def sim(v_x: int, v_y: int, x_min: int, x_max: int, y_min: int, y_max: int) -> bool:
    x, y = 0, 0
    while x <= x_max and y >= y_min:
        x += v_x
        y += v_y
        if x >= x_min and x <= x_max and y >= y_min and y <= y_max:
            return True
        v_x -= 1 if v_x > 0 else 0
        v_y -= 1
    return False

def solution2(x_range: Tuple[int, int], y_range: Tuple[int, int]) -> int:
    x_min, x_max = x_range
    y_min, y_max = y_range
    v_y_min = y_min
    v_y_max = -y_min - 1
    # (v+1)v/2 > x_min
    v_x_min = math.ceil(-.5 + math.sqrt(1 + 8 * x_min)/2)
    v_x_max = x_max
    cnt = 0
    for v_x in range(v_x_min, v_x_max+1):
        for v_y in range(v_y_min, v_y_max+1):
            if sim(v_x, v_y, x_min, x_max, y_min, y_max):
                print((v_x, v_y), end=' ', flush=True)
                cnt += 1
    return cnt
