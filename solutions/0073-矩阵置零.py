# Problem Id:  73
# Problem Name:  Set Matrix Zeroes, 矩阵置零
# Problem Url:  https://leetcode-cn.com/problems/set-matrix-zeroes/
# Problem Level:  Medium
 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        a = 0
        b = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = -999
                    matrix[0][j] = -999
                    if i == 0:
                        a = 1
                    if j == 0:
                        b = 1
        for i in range(1,len(matrix)):
            if matrix[i][0] == -999:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        for j in range(1,len(matrix[0])):
            if matrix[0][j] == -999:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        if b == 1:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if a == 1:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0