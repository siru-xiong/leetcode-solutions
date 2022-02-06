# Problem Id:  118
# Problem Name:  Pascal's Triangle, 杨辉三角
# Problem Url:  https://leetcode-cn.com/problems/pascals-triangle/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def temp_sum(self, row: List[int]) -> List[int]:
        length = len(row)
        row = [0] + row + [0]
        result = [0] * (length + 1)
        for i in range(length+1):
            result[i] = row[i] + row[i+1]
        return result
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            result = [[1]]
            for i in range(numRows-1):
                result = result + [Solution().temp_sum(result[i])]
            return result
