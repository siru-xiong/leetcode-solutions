# Problem Id:  495
# Problem Name:  Teemo Attacking, 提莫攻击
# Problem Url:  https://leetcode-cn.com/problems/teemo-attacking/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        left = timeSeries[0]+duration-1
        for i in range(len(timeSeries)-1):
            if timeSeries[i]+duration-1 < timeSeries[i+1]:
                res = res + duration
            else:
                res = res + timeSeries[i+1]-timeSeries[i]
        res = res + duration
        return res
