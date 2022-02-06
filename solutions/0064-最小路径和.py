# Problem Id:  64
# Problem Name:  Minimum Path Sum, 最小路径和
# Problem Url:  https://leetcode-cn.com/problems/minimum-path-sum/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        res = {}
        res[(0,0)] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i+j != 0:
                    res[(i,j)] = min(res.get((i-1,j),float('inf')),res.get((i,j-1),float('inf')))+grid[i][j]
        return res[(len(grid)-1,len(grid[0])-1)]