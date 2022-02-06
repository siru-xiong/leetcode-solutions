-- Problem Id:  184
-- Problem Name:  Department Highest Salary, 部门工资最高的员工
-- Problem Url:  https://leetcode-cn.com/problems/department-highest-salary/
-- Problem Level:  Medium
-- Language:  MySQL
 
# Write your MySQL query statement below
select d.Name as Department, e.Name as Employee , e.Salary
from Employee as e
inner join Department as d 
on e.DepartmentId = d.Id
where (e.Salary , e.DepartmentId) in
(
    select max(e2.Salary),e2.DepartmentId
    from Employee as e2
    group by e2.DepartmentId
)