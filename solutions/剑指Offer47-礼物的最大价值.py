# Problem Id:  剑指 Offer 47
# Problem Name:  礼物的最大价值 LCOF, 礼物的最大价值
# Problem Url:  https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = []
        for i in range(m):
            res.append([0]*n)
        res[0][0] = grid[0][0]
        for i in range(1,m):
            res[i][0] = res[i-1][0] + grid[i][0]
        for i in range(1,n):
            res[0][i] = res[0][i-1] + grid[0][i]
        for i in range(1,m):
            for j in range(1,n):
                res[i][j] = max(res[i-1][j],res[i][j-1])+grid[i][j]
        return res[-1][-1]