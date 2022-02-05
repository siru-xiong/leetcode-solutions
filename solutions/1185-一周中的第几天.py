# Problem Id:  1185
# Problem Name:  Day of the Week, 一周中的第几天
# Problem Url:  https://leetcode-cn.com/problems/day-of-the-week/
# Problem Level:  Easy
 
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        if month == 1 or month == 2:
            month = month + 12
            year = year - 1

        c = year // 100
        y = year % 100
        m = month
        d = day

        D = int(c/4)-2*c+y+int(y/4)+int(13*(m+1)/5)+d - 1
        W = D % 7
        result = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return result[W]