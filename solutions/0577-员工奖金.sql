# Problem Id:  577
# Problem Name:  Employee Bonus, 员工奖金
# Problem Url:  https://leetcode-cn.com/problems/employee-bonus/
# Problem Level:  Easy
 
# Write your MySQL query statement below
select name, bonus
from Employee
left join Bonus
on Employee.empid = Bonus.empid
where Bonus.bonus < 1000 or Bonus.bonus is NULL