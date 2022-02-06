# Problem Id:  509
# Problem Name:  Fibonacci Number, 斐波那契数
# Problem Url:  https://leetcode-cn.com/problems/fibonacci-number/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
     def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            result = [-1] * (n+1)
            result[0] = 0
            result[1] = 1
            for i in range(2,n+1):
                result[i] = result[i-1] + result[i-2]
            return result[-1]