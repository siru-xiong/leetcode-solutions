# Problem Id:  343
# Problem Name:  Integer Break, 整数拆分
# Problem Url:  https://leetcode-cn.com/problems/integer-break/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def integerBreak(self, n: int) -> int:
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