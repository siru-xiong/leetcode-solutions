# Problem Id:  剑指 Offer 10- I
# Problem Name:  斐波那契数列  LCOF, 斐波那契数列
# Problem Url:  https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a , b = 0 , 1
            for i in range(n - 1):
                a , b = b % 1000000007, (a+b) % 1000000007
            return b