# Problem Id:  807
# Problem Name:  Max Increase to Keep City Skyline, 保持城市天际线
# Problem Url:  https://leetcode-cn.com/problems/max-increase-to-keep-city-skyline/
# Problem Level:  Medium
 
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        s1 = [max(i) for i in grid]
        s2 = [max([i[j] for i in grid]) for j in range(len(grid[0]))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                res = res + min(s1[i],s2[j]) - grid[i][j]
        return res