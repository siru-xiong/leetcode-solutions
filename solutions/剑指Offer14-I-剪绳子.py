# Problem Id:  剑指 Offer 14- I
# Problem Name:  剪绳子  LCOF, 剪绳子
# Problem Url:  https://leetcode-cn.com/problems/jian-sheng-zi-lcof/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        a = n // 3
        r = n % 3
        if r == 0:
            return 3 ** a
        elif r == 1:
            return 3 ** (a-1) * 4
        else:
            return 3 ** a * 2