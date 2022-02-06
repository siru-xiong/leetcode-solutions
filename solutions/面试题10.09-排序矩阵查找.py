# Problem Id:  面试题 10.09
# Problem Name:  Sorted Matrix Search LCCI, 排序矩阵查找
# Problem Url:  https://leetcode-cn.com/problems/sorted-matrix-search-lcci/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        i = 0
        j = len(matrix[0])-1
        while i < len(matrix) and j > -1:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False