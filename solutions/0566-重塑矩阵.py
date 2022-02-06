# Problem Id:  566
# Problem Name:  Reshape the Matrix, 重塑矩阵
# Problem Url:  https://leetcode-cn.com/problems/reshape-the-matrix/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]):
            return mat
        matrix=[[0 for i in range(c)] for i in range(r)]
        res=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res.append(mat[i][j])
        z=0
        for i in range(r):
            for j in range(c):
                matrix[i][j]=res[z]
                z+=1
        return matrix