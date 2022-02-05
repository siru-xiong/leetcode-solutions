# Problem Id:  693
# Problem Name:  Binary Number with Alternating Bits, 交替位二进制数
# Problem Url:  https://leetcode-cn.com/problems/binary-number-with-alternating-bits/
# Problem Level:  Easy
 
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = n & 1
        n = n >> 1
        while n != 0:
            now = n & 1
            n = n >> 1
            if last == now:
                return False
            else:
                last = now
        return True