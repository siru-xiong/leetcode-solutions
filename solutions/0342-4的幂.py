# Problem Id:  342
# Problem Name:  Power of Four, 4的幂
# Problem Url:  https://leetcode-cn.com/problems/power-of-four/
# Problem Level:  Easy
 
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 4 == 0:
            n = n // 4
        return n == 1
