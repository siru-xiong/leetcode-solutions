# Problem Id:  171
# Problem Name:  Excel Sheet Column Number, Excel 表列序号
# Problem Url:  https://leetcode-cn.com/problems/excel-sheet-column-number/
# Problem Level:  Easy
 
class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for x in s:
            ans *= 26
            ans += ord(x)-ord('A')+1
        return ans