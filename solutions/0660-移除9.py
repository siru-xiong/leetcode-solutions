# Problem Id:  660
# Problem Name:  Remove 9, 移除 9
# Problem Url:  https://leetcode-cn.com/problems/remove-9/
# Problem Level:  Hard
 
class Solution:
    def newInteger(self, n: int) -> int:
        t = 1
        while t*9 <= n:
            t *= 9
        res = 0
        while t != 0:
            res = res*10 + n // t
            n %= t
            t //= 9
        return res