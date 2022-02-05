# Problem Id:  463
# Problem Name:  Island Perimeter, 岛屿的周长
# Problem Url:  https://leetcode-cn.com/problems/island-perimeter/
# Problem Level:  Easy
 
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    result = result + 4
                    for a,b in [i-1,j],[i+1,j],[i,j-1],[i,j+1]:
                            if a>=0 and a<len(grid) and b>=0 and b<len(grid[0]):
                                result = result - grid[a][b]
        return result
