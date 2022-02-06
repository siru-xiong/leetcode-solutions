# Problem Id:  240
# Problem Name:  Search a 2D Matrix II, 搜索二维矩阵 II
# Problem Url:  https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        result = False
        i = 0
        j = len(matrix[0])-1
        while i<=len(matrix)-1 and j>=0:
            if matrix[i][j] == target:
                result = True
                break
            elif matrix[i][j] > target:
                j = j - 1
            else:
                i = i + 1
        return result