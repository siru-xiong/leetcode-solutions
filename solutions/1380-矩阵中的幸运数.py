# Problem Id:  1380
# Problem Name:  Lucky Numbers in a Matrix, 矩阵中的幸运数
# Problem Url:  https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix/
# Problem Level:  Easy
 
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(matrix)):
            vm = min(matrix[i])
            t = -1
            for j in range(len(matrix[i])):
                if matrix[i][j] == vm:
                    t = j
                    break
            vmax = max([x[t] for x in matrix])
            if matrix[i][t] == vmax:
                res.append(matrix[i][t])
        return res