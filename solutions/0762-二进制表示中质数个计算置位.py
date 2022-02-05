# Problem Id:  762
# Problem Name:  Prime Number of Set Bits in Binary Representation, 二进制表示中质数个计算置位
# Problem Url:  https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation/
# Problem Level:  Easy
 
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        a = set([2,3,5,7,11,13,17,19])
        b = list(bin(L)[2:])
        base = 0
        res = 0
        for i in b:
            if i == '1':
                base += 1
        if base in a:
            res += 1
        while L+1 <= R:
            L = L + 1
            index = 0
            t = 0
            for i in range(1,len(b)+1):
                if b[-i] == '1':
                    b[-i] = '0'
                    index = -i
                    t = t + 1
                else:
                    break
            if index == 0:
                base = base + 1
                if base in a:
                    res += 1
                b[-1] = '1'
            elif index != - len(b):
                base = base + 1 - t
                if base in a:
                    res += 1
                b[index-1] = '1'
            else:
                base = 1
                b = ['1'] + ['0'] * len(b)
        return res



            