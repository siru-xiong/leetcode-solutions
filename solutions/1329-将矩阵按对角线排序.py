# Problem Id:  1329
# Problem Name:  Sort the Matrix Diagonally, 将矩阵按对角线排序
# Problem Url:  https://leetcode-cn.com/problems/sort-the-matrix-diagonally/
# Problem Level:  Medium
 
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        for i in range(m-1,-1,-1):
            res = [mat[i][0]]
            k = 1
            while i + k < m and k < n:
                res.append(mat[i+k][k])
                k = k + 1
            res.sort()
            for j in range(len(res)):
                mat[i+j][j] = res[j]

        for i in range(1,n):
            res = [mat[0][i]]
            k = 1
            while k < m and i + k < n:
                res.append(mat[k][i+k])
                k = k + 1
            res.sort()
            for j in range(len(res)):
                mat[j][i+j] = res[j]

        return mat
