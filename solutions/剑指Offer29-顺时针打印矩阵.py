# Problem Id:  剑指 Offer 29
# Problem Name:  顺时针打印矩阵  LCOF, 顺时针打印矩阵
# Problem Url:  https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/
# Problem Level:  Easy
 
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
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