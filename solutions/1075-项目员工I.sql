# Problem Id:  1075
# Problem Name:  Project Employees I, 项目员工 I
# Problem Url:  https://leetcode-cn.com/problems/project-employees-i/
# Problem Level:  Easy
 
# Write your MySQL query statement below
select b.project_id, round(avg(a.experience_years),2) as average_years from
Employee a
inner join Project b
on a.employee_id = b.employee_id
group by project_id