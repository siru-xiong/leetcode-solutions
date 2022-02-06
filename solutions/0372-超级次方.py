# Problem Id:  372
# Problem Name:  Super Pow, 超级次方
# Problem Url:  https://leetcode-cn.com/problems/super-pow/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def __init__(self):
        self.rec = {}
        self.reca = {}
    def sup(self,a,b):
        if b == 0:
            self.rec[0] = a
            return a % 1337
        elif b == 1:
            if 1 in self.rec:
                return self.rec[1]
            t = 1
            for i in range(10):
                t *= a
                t %= 1337
            t %= 1337
            self.rec[1] = t
            return t
        else:
            a %= 1337
            t = self.sup(a,b-1)
            s = 1
            for i in range(10):
                s *= t
                s %= 1337
            s %= 1337
            self.rec[b] = s
            return s

    def superPow(self, a: int, b: List[int]) -> int:
        t = self.sup(a,len(b)-1)
        for i in self.rec:
            self.reca[(i,0)] = 1
            q = 1
            for j in range(1,10):
                q = (q*self.rec[i]) % 1337
                self.reca[(i,j)] = q
        return self.superPowp(a,b)

    def superPowp(self, a: int, b: List[int]) -> int:
        if len(b) == 1:
            if b[0] == 0:
                return 1
            else:
                t = 1
                a = a % 1337
                for i in range(b[0]):
                    t *= a
                    t %= 1337
                t %= 1337
                return t
        else:
            a = a % 1337
            right = self.superPowp(a,b[1:]) % 1337
            t = self.reca[(len(b)-1,b[0])]
            #t = ((self.rec[len(b)-1] % 1337)** b[0]) % 1337
            return (right*t) % 1337