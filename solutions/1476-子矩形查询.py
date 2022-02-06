# Problem Id:  1476
# Problem Name:  Subrectangle Queries, 子矩形查询
# Problem Url:  https://leetcode-cn.com/problems/subrectangle-queries/
# Problem Level:  Medium
# Language:  Python3
 
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rec = rectangle
        self.nr = len(self.rec)
        self.nc = len(self.rec[0])
        self.up = []
        self.vl = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.up.append([row1,col1,row2,col2])
        self.vl.append(newValue)

    def getValue(self, row: int, col: int) -> int:
        for i in range(1,len(self.up)+1):
            if (row >= self.up[-i][0]) and (row <= self.up[-i][2]) and (col >= self.up[-i][1]) and (col <= self.up[-i][3]):
                return self.vl[-i]
                break
        return self.rec[row][col]



# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)