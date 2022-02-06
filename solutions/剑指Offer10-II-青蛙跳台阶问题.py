# Problem Id:  剑指 Offer 10- II
# Problem Name:  青蛙跳台阶问题  LCOF, 青蛙跳台阶问题
# Problem Url:  https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1
        else:
            x , y = 1 , 1
            for i in range(n-1):
                x , y = y , (x+y) % 1000000007
            return y