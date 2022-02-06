-- Problem Id:  176
-- Problem Name:  Second Highest Salary, 第二高的薪水
-- Problem Url:  https://leetcode-cn.com/problems/second-highest-salary/
-- Problem Level:  Medium
-- Language:  MySQL
 
# Write your MySQL query statement below
select max(Salary) as SecondHighestSalary
from Employee
where Salary != (select max(Salary) from Employee)