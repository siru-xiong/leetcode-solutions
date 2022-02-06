# Problem Id:  1266
# Problem Name:  Minimum Time Visiting All Points, 访问所有点的最小时间
# Problem Url:  https://leetcode-cn.com/problems/minimum-time-visiting-all-points/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        vsum = 0
        for i in range(1,len(points)):
            x = abs(points[i][0]-points[i-1][0])
            y = abs(points[i][1]-points[i-1][1])
            vsum = vsum + min(x,y) + abs(x-y)
        return vsum
