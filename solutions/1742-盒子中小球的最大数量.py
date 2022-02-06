# Problem Id:  1742
# Problem Name:  Maximum Number of Balls in a Box, 盒子中小球的最大数量
# Problem Url:  https://leetcode-cn.com/problems/maximum-number-of-balls-in-a-box/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ct = {}
        base = sum([int(x) for x in str(lowLimit)])
        ct[base] = ct.get(base,0) + 1
        for i in range(lowLimit+1,highLimit+1):
            x = 0
            t = i
            while t % 10 == 0:
                x = x + 1
                t = t // 10
            base = base + 1 - 9*x
            ct[base] = ct.get(base,0) + 1
        res = 0
        for i in ct:
            if ct[i] > res:
                res = ct[i]
        return res
