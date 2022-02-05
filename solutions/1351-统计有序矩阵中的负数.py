# Problem Id:  1351
# Problem Name:  Count Negative Numbers in a Sorted Matrix, 统计有序矩阵中的负数
# Problem Url:  https://leetcode-cn.com/problems/count-negative-numbers-in-a-sorted-matrix/
# Problem Level:  Easy
 
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            if grid[i][-1] >= 0:
                pass
            elif grid[i][0] < 0:
                count = count + len(grid[i])
            else:
                left = 0
                right = len(grid[i])-1
                while right - left >= 2:
                    med = int((left+right)/2)
                    if grid[i][med] >= 0:
                        left = med
                    else:
                        right = med
                if grid[i][left] < 0:
                    count = count + len(grid[i])-left
                else:
                    count = count + len(grid[i])-right
        return count