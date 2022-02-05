# Problem Id:  剑指 Offer 14- II
# Problem Name:  剪绳子 II LCOF, 剪绳子 II
# Problem Url:  https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/
# Problem Level:  Medium
 
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        a = n // 3
        r = n % 3
        if r == 0:
            res = 1
            for i in range(a):
                res = res * 3
                res = res % 1000000007
            return res
        elif r == 1:
            res = 1
            for i in range(a-1):
                res = res * 3
                res = res % 1000000007
            res = res * 4
            return res % 1000000007
        else:
            res = 1
            for i in range(a):
                res = res * 3
                res = res % 1000000007
            res = res * 2
            return res % 1000000007