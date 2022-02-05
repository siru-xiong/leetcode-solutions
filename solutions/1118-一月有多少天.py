# Problem Id:  1118
# Problem Name:  Number of Days in a Month, 一月有多少天
# Problem Url:  https://leetcode-cn.com/problems/number-of-days-in-a-month/
# Problem Level:  Easy
 
class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
            return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1] 
        else:
            return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month- 1]