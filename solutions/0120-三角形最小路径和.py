# Problem Id:  120
# Problem Name:  Triangle, 三角形最小路径和
# Problem Url:  https://leetcode-cn.com/problems/triangle/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        for i in range(1,m):
            for j in range(i+1):
                t = float('inf')
                if j <= i-1:
                    t = min(t,triangle[i-1][j])
                if j-1 >= 0:
                    t = min(t,triangle[i-1][j-1])
                triangle[i][j] += t
        return min(triangle[-1])