-- Problem Id:  569
-- Problem Name:  Median Employee Salary, 员工薪水中位数
-- Problem Url:  https://leetcode-cn.com/problems/median-employee-salary/
-- Problem Level:  Hard
-- Language:  MySQL
 
# Write your MySQL query statement below
select Id, Company, Salary from 
(select Id, Company, Salary,
row_number() over (partition by Company order by Salary,id ) as p_num,
row_number() over (partition by Company order by Salary desc,id desc) as n_num
from Employee) as n
where n.p_num = n.n_num
or n.p_num = n.n_num+1 or n.n_num = n.p_num+1