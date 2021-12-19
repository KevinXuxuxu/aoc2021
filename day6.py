class LanternFishCounter:

    def __init__(self, s: str):
        self.d = [0] * 9
        for i in range(9):
            self.d[i] = 0
        for n in s.split(','):
            self.d[int(n)] += 1

    def shift(self):
        s0 = self.d[0]
        for i in range(1, 9):
            self.d[i - 1] = self.d[i]
        self.d[6] += s0
        self.d[8] = s0

def solution(s: str, days: int) -> int:
    LFC = LanternFishCounter(s)
    for i in range(days):
        LFC.shift()
    return sum(LFC.d)
