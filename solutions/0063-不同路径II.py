# Problem Id:  63
# Problem Name:  Unique Paths II, 不同路径 II
# Problem Url:  https://leetcode-cn.com/problems/unique-paths-ii/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = []
        for i in range(m):
            res.append([0]*n)
        index = 0
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                index = 1
            if index == 0:
                res[0][i] = 1
        index = 0
        for j in range(m):
            if obstacleGrid[j][0] == 1:
                index = 1
            if index == 0:
                res[j][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]
                    
            