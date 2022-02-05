# Problem Id:  231
# Problem Name:  Power of Two, 2 的幂
# Problem Url:  https://leetcode-cn.com/problems/power-of-two/
# Problem Level:  Easy
 
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        x = 2
        result = True
        while n != 1:
            if n % 2 != 0:
                result = False
                break
            else:
                n = n // 2
        return result