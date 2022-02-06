# Problem Id:  74
# Problem Name:  Search a 2D Matrix, 搜索二维矩阵
# Problem Url:  https://leetcode-cn.com/problems/search-a-2d-matrix/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m - 1
        while r - l > 1:
            med = int((l+r)/2)
            if matrix[med][0] > target:
                r = med - 1
            elif matrix[med][0] < target:
                l = med
            else:
                return True
        if matrix[r][0] < target:
            tr = r
        elif matrix[r][0] > target:
            tr = l
        else:
            return True
        l = 0
        r = n - 1
        while r - l > 1:
            med = int((l+r)/2)
            if matrix[tr][med] > target:
                r = med - 1
            elif matrix[tr][med] < target:
                l = med + 1
            else:
                return True
        return matrix[tr][l] == target or matrix[tr][r] == target