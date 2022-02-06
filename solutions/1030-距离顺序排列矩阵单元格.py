# Problem Id:  1030
# Problem Name:  Matrix Cells in Distance Order, 距离顺序排列矩阵单元格
# Problem Url:  https://leetcode-cn.com/problems/matrix-cells-in-distance-order/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        result = []
        for i in range(R):
            for j in range(C):
                result.append([i,j])
        result.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return result  

        