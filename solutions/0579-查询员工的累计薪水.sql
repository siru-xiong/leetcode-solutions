-- Problem Id:  579
-- Problem Name:  Find Cumulative Salary of an Employee, 查询员工的累计薪水
-- Problem Url:  https://leetcode-cn.com/problems/find-cumulative-salary-of-an-employee/
-- Problem Level:  Hard
-- Language:  MySQL
 
# Write your MySQL query statement below
select r.id, r.month, r.s1+r.s2+r.s3 as salary from
(
select t1.id, t1.month, t1.salary as s1, CASE WHEN t2.salary IS NULl THEN 0 ELSE t2.salary END as s2, CASE WHEN t3.salary IS NULl THEN 0 ELSE t3.salary END as s3
from employee  t1
left join employee  t2
on t1.id = t2.id and t1.month = t2.month + 1
left join employee  t3
on t1.id = t3.id and t1.month = t3.month + 2
) r
where
(id,month) not in 
(
select id, max(month) from employee group by id
)
order by id, month desc