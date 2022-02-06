# Problem Id:  1344
# Problem Name:  Angle Between Hands of a Clock, 时钟指针的夹角
# Problem Url:  https://leetcode-cn.com/problems/angle-between-hands-of-a-clock/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if minutes == 0:
            if hour == 12:
                return 0
            else:
                return min(hour * 30 ,360 - hour*30)
        else:
            if hour == 12:
                hour = 0
            m = (minutes / 60.0) * 360
            h = hour * 30 + (minutes / 60.0) * 30
            t = max(m,h) - min(m,h)
            return min(t,360-t)
