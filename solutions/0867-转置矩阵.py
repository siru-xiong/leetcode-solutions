# Problem Id:  867
# Problem Name:  Transpose Matrix, 转置矩阵
# Problem Url:  https://leetcode-cn.com/problems/transpose-matrix/
# Problem Level:  Easy
 
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        m = len(A)
        n = len(A[0])
        result = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp = temp + [A[j][i]]
            result = result + [temp]
        return result