# Problem Id:  1732
# Problem Name:  Find the Highest Altitude, 找到最高海拔
# Problem Url:  https://leetcode-cn.com/problems/find-the-highest-altitude/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        a = 0
        for i in range(len(gain)):
            a += gain[i]
            res = max(res,a)
        return res