# Problem Id:  1154
# Problem Name:  Day of the Year, 一年中的第几天
# Problem Url:  https://leetcode-cn.com/problems/day-of-the-year/
# Problem Level:  Easy
 
class Solution:
    def dayOfYear(self, date: str) -> int:
        index = 0
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:])
        if year % 4 == 0 and year % 100!= 0 or year % 400 == 0:
            index = 1
        if index == 1:
            temp = [0,31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            temp = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        return sum(temp[0:month])+day
