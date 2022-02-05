# Problem Id:  892
# Problem Name:  Surface Area of 3D Shapes, 三维形体的表面积
# Problem Url:  https://leetcode-cn.com/problems/surface-area-of-3d-shapes/
# Problem Level:  Easy
 
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != 0:
                    res = res + 2
                if i - 1 >= 0:
                    res = res + max(grid[i][j]-grid[i-1][j],0)
                else:
                    res = res + grid[i][j]
                if i + 1 <= len(grid)-1:
                    res = res + max(grid[i][j]-grid[i+1][j],0)
                else:
                    res = res + grid[i][j]
                if j - 1 >= 0:
                    res = res + max(grid[i][j]-grid[i][j-1],0)
                else:
                    res = res + grid[i][j]
                if j + 1 <= len(grid)-1:
                    res = res + max(grid[i][j]-grid[i][j+1],0)
                else:
                    res = res + grid[i][j]
        return res