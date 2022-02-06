# Problem Id:  551
# Problem Name:  Student Attendance Record I, 学生出勤记录 I
# Problem Url:  https://leetcode-cn.com/problems/student-attendance-record-i/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        b = 0
        for i in range(len(s)):
            if s[i] == 'A':
                a += 1
        for i in range(len(s)-2):
            if s[i] == 'L' and s[i+1] == 'L' and s[i+2] == 'L':
                return False
        return a <= 1