# Problem Id:  190
# Problem Name:  Reverse Bits, 颠倒二进制位
# Problem Url:  https://leetcode-cn.com/problems/reverse-bits/
# Problem Level:  Easy
 
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        t = 31
        while n:
            res += (n & 1) << t
            n >>= 1
            t -= 1
        return res