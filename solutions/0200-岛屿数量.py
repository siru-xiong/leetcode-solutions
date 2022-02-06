# Problem Id:  200
# Problem Name:  Number of Islands, 岛屿数量
# Problem Url:  https://leetcode-cn.com/problems/number-of-islands/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res = res + 1
                    t = set([(i,j)])
                    grid[i][j] = '0'
                    lent = 1
                    while True:
                        s = set()
                        for k in t:
                            r = [[k[0]-1,k[1]],[k[0]+1,k[1]],[k[0],k[1]-1],[k[0],k[1]+1]]
                            for co in r:
                                if co[0] >=0 and co[0] < len(grid) and co[1] >= 0 and co[1] < len(grid[0]):
                                    if grid[co[0]][co[1]] == '1':
                                        s.add((co[0],co[1]))
                                        grid[co[0]][co[1]] = '0'
                        t = t | s
                        if len(t) == lent:
                            break
                        else:
                            lent = len(t)

        return res
            
    