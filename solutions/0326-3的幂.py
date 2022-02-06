# Problem Id:  326
# Problem Name:  Power of Three, 3 的幂
# Problem Url:  https://leetcode-cn.com/problems/power-of-three/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            while n % 3 == 0:
                n = n // 3
            return n == 1