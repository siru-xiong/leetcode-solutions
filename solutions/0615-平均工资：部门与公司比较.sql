# Problem Id:  615
# Problem Name:  Average Salary: Departments VS Company, 平均工资：部门与公司比较
# Problem Url:  https://leetcode-cn.com/problems/average-salary-departments-vs-company/
# Problem Level:  Hard
 
# Write your MySQL query statement below
select t2.pay_month, t2.department_id, case when t2.amount > t.aa then 'higher' when t2.amount = t.aa then 'same' else 'lower' end as comparison from 
(
select department_id,substring(pay_date,1,7) as pay_month, avg(amount) as amount
from salary
inner join
employee
on salary.employee_id = employee.employee_id
group by department_id,substring(pay_date,1,7) ) t2
inner join
(
select substring(pay_date,1,7) as pay_month, avg(amount) as aa
from salary
group by substring(pay_date,1,7)
) t
on t.pay_month = t2.pay_month

