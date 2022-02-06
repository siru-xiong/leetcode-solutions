# Problem Id:  1637
# Problem Name:  Widest Vertical Area Between Two Points Containing No Points, 两点之间不包含任何点的最宽垂直面积
# Problem Url:  https://leetcode-cn.com/problems/widest-vertical-area-between-two-points-containing-no-points/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        a = sorted([i[0] for i in points])
        t = 0
        for i in range(1,len(a)):
            if a[i]-a[i-1] > t:
                t = a[i] - a[i-1]
        return t