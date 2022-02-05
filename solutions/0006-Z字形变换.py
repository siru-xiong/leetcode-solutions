# Problem Id:  6
# Problem Name:  ZigZag Conversion, Z 字形变换
# Problem Url:  https://leetcode-cn.com/problems/zigzag-conversion/
# Problem Level:  Medium
 
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ct = {}
        j = 0
        dire = 1
        for i in s:
            ct[j] = ct.get(j,'') + i
            if j == numRows-1 and dire == 1:
                dire = -dire
            if j == 0 and dire == -1:
                dire = -dire
            j = j + dire
        re = ''
        for k in range(numRows):
            re = re + ct.get(k,'')
        return re
