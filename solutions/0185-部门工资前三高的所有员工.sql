# Problem Id:  185
# Problem Name:  Department Top Three Salaries, 部门工资前三高的所有员工
# Problem Url:  https://leetcode-cn.com/problems/department-top-three-salaries/
# Problem Level:  Hard
 
# Write your MySQL query statement below
select d.Name as Department, e.Name as Employee , e.Salary
from Employee as e, Department as d 
where e.DepartmentId = d.Id
and e.Salary >=
(
    select MIN(t.Salary) from (
    select d2.Salary 
    from Employee as d2
    where d2.DepartmentId = e.DepartmentId
    GROUP BY d2.Salary
    ORDER BY d2.Salary DESC
    LIMIT 3 ) as t
    
)


#select d.Name as Department,e1.Name as Employee,e1.Salary 
# from Employee e1 join employee e2 on e1.DepartmentId=e2.DepartmentId
#join Department d on e1.DepartmentId =d.Id 
#where e1.salary<=e2.salary 
#group by e1.id having count(distinct e2.salary)<=3