# Problem Id:  1314
# Problem Name:  Matrix Block Sum, 矩阵区域和
# Problem Url:  https://leetcode-cn.com/problems/matrix-block-sum/
# Problem Level:  Medium
 
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        a = 0
        m = len(mat)
        n = len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i <= K and j <= K:
                    a = a + mat[i][j]
        res = []
        for i in range(m):
            res.append([0]*n)
        
        res[0][0] = a

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i != 0 or j != 0:
                    if j != 0:
                        t = 0
                        for r in range(i-K,i+K+1):
                            if r >= 0 and r < m:
                                if j + K >= 0 and j + K < n:
                                    t += mat[r][j+K]
                                if j - K - 1>= 0 and j - K - 1< n:
                                    t -= mat[r][j-K-1]
                        res[i][j] = res[i][j-1]+t
                    else:
                        t = 0
                        for c in range(j-K,j+K+1):
                            if c >= 0 and c < n:
                                if i + K >= 0 and i + K < m:
                                    t += mat[i+K][c]
                                if i - 1 - K >= 0 and i - 1 - K < m:
                                    t -= mat[i-1-K][c]
                        res[i][j] = res[i-1][j]+t
        return res






