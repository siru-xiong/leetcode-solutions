# Problem Id:  剑指 Offer 04
# Problem Name:  二维数组中的查找 LCOF, 二维数组中的查找
# Problem Url:  https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
# Problem Level:  Medium
 
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [] or matrix == [[]]:
            return False
        i = 0
        j = len(matrix[0])-1
        while True:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
            if i == len(matrix) or j == -1:
                return False