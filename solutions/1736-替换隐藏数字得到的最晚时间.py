# Problem Id:  1736
# Problem Name:  Latest Time by Replacing Hidden Digits, 替换隐藏数字得到的最晚时间
# Problem Url:  https://leetcode-cn.com/problems/latest-time-by-replacing-hidden-digits/
# Problem Level:  Easy
 
class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        if time[0] == '?':
            if time[1] != '?' and int(time[1]) >= 4:
                time[0] = '1'
            else:
                time[0] = '2'
        if time[1] == '?':
            if time[0] == '0' or time[0] == '1':
                time[1] = '9'
            else:
                time[1] = '3'
        if time[3] == '?':
            time[3] = '5'
        if time[4] == '?':
            time[4] = '9'
        return ''.join(time)