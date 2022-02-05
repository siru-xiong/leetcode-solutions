# Problem Id:  119
# Problem Name:  Pascal's Triangle II, 杨辉三角 II
# Problem Url:  https://leetcode-cn.com/problems/pascals-triangle-ii/
# Problem Level:  Easy
 
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            result = [1] * (rowIndex + 1)
            for i in range(1,rowIndex):
                result[i] = int (result[i-1] * (rowIndex-i+1) / i )
            return result
