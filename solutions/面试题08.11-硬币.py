# Problem Id:  面试题 08.11
# Problem Name:  Coin LCCI, 硬币
# Problem Url:  https://leetcode-cn.com/problems/coin-lcci/
# Problem Level:  Medium
 
class Solution:
    def waysToChange(self, n: int) -> int:
        res = 0
        for i in range((n // 25)+1):
            r = n - 25 * i
            a = r // 10
            b = (r % 10) // 5
            res += (a+1)*(a+b+1)
            res = res % 1000000007
        return res

