# Problem Id:  54
# Problem Name:  Spiral Matrix, 螺旋矩阵
# Problem Url:  https://leetcode-cn.com/problems/spiral-matrix/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        dire = [[0,1],[1,0],[0,-1],[-1,0]]
        j = 0
        re = []
        start = [0,0]
        while start[0] < m and start[0] >= 0 and start[1] < n and start[1]>= 0 and matrix[start[0]][start[1]] != -999:
            if matrix[start[0]][start[1]] != -999:
                re.append(matrix[start[0]][start[1]])
                matrix[start[0]][start[1]] = -999
            if start[0] + dire[j][0] >= m or start[0] + dire[j][0] < 0 or start[1] + dire[j][1] >= n or start[1] + dire[j][1] < 0 or matrix[start[0] + dire[j][0]][start[1] + dire[j][1]] == -999:
                j = (j+1) % 4
            start[0] += dire[j][0]
            start[1] += dire[j][1]
        return re