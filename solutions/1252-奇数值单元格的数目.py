# Problem Id:  1252
# Problem Name:  Cells with Odd Values in a Matrix, 奇数值单元格的数目
# Problem Url:  https://leetcode-cn.com/problems/cells-with-odd-values-in-a-matrix/
# Problem Level:  Easy
 
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row = {}
        col = {}
        for i in indices:
            row[i[0]] = row.get(i[0],0)+1
            col[i[1]] = col.get(i[1],0)+1
        res = 0
        for i in range(n):
            for j in range(m):
                if (row.get(i,0)+col.get(j,0)) % 2 == 1:
                    res = res + 1
        return res
