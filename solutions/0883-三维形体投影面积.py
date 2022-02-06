# Problem Id:  883
# Problem Name:  Projection Area of 3D Shapes, 三维形体投影面积
# Problem Url:  https://leetcode-cn.com/problems/projection-area-of-3d-shapes/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        z = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    z = z + 1
        x = sum([max(i) for i in grid])
        y = sum([max([i[j] for i in grid]) for j in range(len(grid))])
        return x+y+z
