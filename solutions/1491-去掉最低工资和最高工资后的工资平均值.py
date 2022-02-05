# Problem Id:  1491
# Problem Name:  Average Salary Excluding the Minimum and Maximum Salary, 去掉最低工资和最高工资后的工资平均值
# Problem Url:  https://leetcode-cn.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
# Problem Level:  Easy
 
class Solution:
    def average(self, salary: List[int]) -> float:
        vmax = float('-inf')
        vmin = float('inf')
        vsum = 0
        for i in range(len(salary)):
            if salary[i] > vmax:
                vmax = salary[i]
            if salary[i] < vmin:
                vmin = salary[i]
            vsum = vsum + salary[i]
        vsum = vsum - vmax - vmin
        return vsum / (len(salary)-2)