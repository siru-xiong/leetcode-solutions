-- Problem Id:  181
-- Problem Name:  Employees Earning More Than Their Managers, 超过经理收入的员工
-- Problem Url:  https://leetcode-cn.com/problems/employees-earning-more-than-their-managers/
-- Problem Level:  Easy
-- Language:  MySQL
 
# Write your MySQL query statement below
select e1.Name as Employee
from Employee as e1, Employee as e2
where e1.ManagerId = e2.Id
and e1.Salary > e2.Salary