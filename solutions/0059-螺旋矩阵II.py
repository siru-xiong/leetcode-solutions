# Problem Id:  59
# Problem Name:  Spiral Matrix II, 螺旋矩阵 II
# Problem Url:  https://leetcode-cn.com/problems/spiral-matrix-ii/
# Problem Level:  Medium
 
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = []
        for i in range(n):
            res.append([-1]*n)
        dire = [[0,1],[1,0],[0,-1],[-1,0]]
        index = 0
        curr = [0,-1]
        for i in range(n*n):
            temp = [curr[0] + dire[index][0] , curr[1] + dire[index][1]]
            if min(temp[0],temp[1]) >= 0 and max(temp[0],temp[1]) <= n-1 and res[temp[0]][temp[1]] == -1:
                res[temp[0]][temp[1]] = i+1
                curr = [temp[0] , temp[1]]
            else:
                index = (index + 1) % 4
                temp = [curr[0] + dire[index][0] , curr[1] + dire[index][1]]
                res[temp[0]][temp[1]] = i+1
                curr = [temp[0] , temp[1]]
        return res