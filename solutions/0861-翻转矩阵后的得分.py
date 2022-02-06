# Problem Id:  861
# Problem Name:  Score After Flipping Matrix, 翻转矩阵后的得分
# Problem Url:  https://leetcode-cn.com/problems/score-after-flipping-matrix/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        for i in range(len(A)):
            if A[i][0] == 0:
                for j in range(len(A[i])):
                    A[i][j] = 1 - A[i][j]
        res = [0] * len(A[0])
        for i in range(len(A[0])):
            t = sum([x[i] for x in A])
            res[i] = max(t,len(A)-t)
        vs = 0
        index = 1
        for i in range(len(res)-1,-1,-1):
            vs = vs + index * res[i]
            index = index * 2
        return vs