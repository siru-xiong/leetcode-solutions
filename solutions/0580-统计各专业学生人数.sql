# Problem Id:  580
# Problem Name:  Count Student Number in Departments, 统计各专业学生人数
# Problem Url:  https://leetcode-cn.com/problems/count-student-number-in-departments/
# Problem Level:  Medium
 
# Write your MySQL query statement below

select dept_name, count(distinct student_id) as student_number
from department
left join student
on department.dept_id = student.dept_id
group by dept_name
order by student_number desc, dept_name