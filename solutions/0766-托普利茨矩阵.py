# Problem Id:  766
# Problem Name:  Toeplitz Matrix, 托普利茨矩阵
# Problem Url:  https://leetcode-cn.com/problems/toeplitz-matrix/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        temp = 0
        for i in range(m):
            start = matrix[i][0]
            for j in range(1,m):
                if i+j <= m-1 and j <= n-1:
                    if matrix[i+j][j] != start:
                        temp = -1
                        break
            if temp == -1:
                break
        
        for i in range(n):
            start = matrix[0][i]
            for j in range(1,n):
                if i+j <= n-1 and j <= m-1:
                    if matrix[j][i+j] != start:
                        temp = -1
                        break
            if temp == -1:
                break
        
        return temp != -1

        