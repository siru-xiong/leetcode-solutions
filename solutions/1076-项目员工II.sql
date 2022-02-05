# Problem Id:  1076
# Problem Name:  Project Employees II, 项目员工II
# Problem Url:  https://leetcode-cn.com/problems/project-employees-ii/
# Problem Level:  Easy
 
# Write your MySQL query statement below
select project_id
from Project
group by project_id
having count(*) = 
(
    select count(*)
    from Project
    group by project_id
    order by count(*) DESC
    limit 1
)