# Problem Id:  面试题 16.05
# Problem Name:  Factorial Zeros LCCI, 阶乘尾数
# Problem Url:  https://leetcode-cn.com/problems/factorial-zeros-lcci/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n <= 4:
            return 0
        res = 0
        t = 1
        while True:
            if t > n:
                t = t // 5
                break
            else:
                t *= 5
        
        while True:
            res += n // t
            t = t // 5
            if t == 1:
                break
        
        return res
        
            