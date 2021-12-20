from typing import List, Tuple

def dec(data: str) -> int:
    return eval('0b' + data)

class Buffer:

    def __init__(self, data: str):
        self.s = data
        self.i = 0

    def read(self, n: int):
        if self.i+n > len(self.s):
            raise ValueError('Σ(oﾟдﾟoﾉ)')
        rtn = self.s[self.i:self.i+n]
        self.i += n
        return rtn

class Packet:
    
    def __init__(self, buffer: Buffer):
        self.v = dec(buffer.read(3))
        self.t = dec(buffer.read(3))
        if self.t == 4:
            self.parse_literal(buffer)
        else:
            lt = buffer.read(1)
            if lt == '0':
                l_remain = dec(buffer.read(15))
                self.parse_op_l(l_remain, buffer)
            else:
                n_remain = dec(buffer.read(11))
                self.parse_op_n(n_remain, buffer)

    def parse_literal(self, buffer: Buffer):
        binary = ''
        while True:
            flag = buffer.read(1)
            binary += buffer.read(4)
            if flag == '0':
                break
        self.value = dec(binary)

    def parse_op_l(self, l: int, buffer: Buffer):
        self.children = []
        sub_buffer = Buffer(buffer.read(l))
        while True:
            try:
                self.children.append(Packet(sub_buffer))
            except ValueError:
                break

    def parse_op_n(self, n: int, buffer: Buffer):
        self.children = []
        for _ in range(n):
            self.children.append(Packet(buffer))

    def __repr__(self) -> str:
        if self.t == 4:
            return str(self.value)
        else:
            return '(op ' + str(self.children) + ')'
            
def solution1(s: str) -> int:
    root = Packet(Buffer(bin(eval('0x' + s))[2:]))
    ans = [0]
    def dfs(p: Packet):
        ans[0] += p.v
        if p.t != 4:
            for child in p.children:
                dfs(child)
    dfs(root)
    return ans[0]

def solution2(s: str) -> int:
    root = Packet(Buffer(bin(eval('0x' + s))[2:]))
    def _eval(p: Packet) -> int:
        if p.t == 0:
            return sum(_eval(c) for c in p.children)
        if p.t == 1:
            rtn = 1
            for c in p.children:
                rtn *= _eval(c)
            return rtn
        if p.t == 2:
            return min(_eval(c) for c in p.children)
        if p.t == 3:
            return max(_eval(c) for c in p.children)
        if p.t == 4:
            return p.value
        if p.t == 5:
            return 1 if _eval(p.children[0]) > _eval(p.children[1]) else 0
        if p.t == 6:
            return 1 if _eval(p.children[0]) < _eval(p.children[1]) else 0
        if p.t == 7:
            return 1 if _eval(p.children[0]) == _eval(p.children[1]) else 0
        raise ValueError(' щ(ﾟДﾟщ)')
    return _eval(root)
