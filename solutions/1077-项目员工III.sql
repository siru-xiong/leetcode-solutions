-- Problem Id:  1077
-- Problem Name:  Project Employees III, 项目员工 III
-- Problem Url:  https://leetcode-cn.com/problems/project-employees-iii/
-- Problem Level:  Medium
-- Language:  MySQL
 
# Write your MySQL query statement below
select project_id, employee_id from
(select b.*, rank() over (partition by b.project_id order by a.experience_years DESC) as r from
Employee a
inner join Project b
on a.employee_id = b.employee_id
) c
where c.r = 1