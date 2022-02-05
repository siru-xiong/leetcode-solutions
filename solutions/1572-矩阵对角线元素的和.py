# Problem Id:  1572
# Problem Name:  Matrix Diagonal Sum, 矩阵对角线元素的和
# Problem Url:  https://leetcode-cn.com/problems/matrix-diagonal-sum/
# Problem Level:  Easy
 
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        a = sum([mat[i][i] for i in range(len(mat))])
        b = sum([mat[i][len(mat)-1-i] for i in range(len(mat))])
        if len(mat) % 2 == 0:
            return a + b
        else:
            return a + b - mat[len(mat) // 2][len(mat) // 2]
