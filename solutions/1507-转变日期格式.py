# Problem Id:  1507
# Problem Name:  Reformat Date, 转变日期格式
# Problem Url:  https://leetcode-cn.com/problems/reformat-date/
# Problem Level:  Easy
 
class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split()
        day = ''.join([x for x in date[0] if x.isdigit()])
        if int(day) < 10:
            day = '0'+day
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].index(date[1]) + 1
        if month < 10:
            month = '0'+str(month)
        else:
            month = str(month)
        year = date[2]
        return year + '-' + month + '-' + day