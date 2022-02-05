# Problem Id:  1700
# Problem Name:  Number of Students Unable to Eat Lunch, 无法吃午餐的学生数量
# Problem Url:  https://leetcode-cn.com/problems/number-of-students-unable-to-eat-lunch/
# Problem Level:  Easy
 
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        t = sum(students)
        f = len(students) - t
        for i in sandwiches:
            if i == 0:
                if f > 0:
                    f = f - 1
                else:
                    break
            else:
                if t > 0:
                    t = t - 1
                else:
                    break
        return t+f