# Problem Id:  221
# Problem Name:  Maximal Square, 最大正方形
# Problem Url:  https://leetcode-cn.com/problems/maximal-square/
# Problem Level:  Medium
 
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        vmax = 0
        seq = [0] * len(matrix[0])
        for i in range(len(matrix[0])):
            if matrix[0][i] == '1':
                seq[i] = 1
                vmax = 1
        for i in range(1,len(matrix)):
            for j in range(len(matrix[i])-1,-1,-1):
                if matrix[i][j] == '1':
                    t1 = seq[j-1]
                    t2 = 0
                    k = 1
                    while i-k >= 0 and matrix[i-k][j] == '1':
                        t2 = t2 + 1
                        k = k + 1
                    t3 = 0
                    h = 1
                    while j-h >= 0 and matrix[i][j-h] == '1':
                        t3 = t3 + 1
                        h = h + 1
                    seq[j] = min(t1,t2,t3)+1
                    if seq[j] > vmax:
                        vmax = seq[j]
                else:
                    seq[j] = 0
        return vmax*vmax
                