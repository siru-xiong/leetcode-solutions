# Problem Id:  1450
# Problem Name:  Number of Students Doing Homework at a Given Time, 在既定时间做作业的学生人数
# Problem Url:  https://leetcode-cn.com/problems/number-of-students-doing-homework-at-a-given-time/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        for i in range(len(startTime)):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                res += 1
        return res