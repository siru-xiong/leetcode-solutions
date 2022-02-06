-- Problem Id:  596
-- Problem Name:  Classes More Than 5 Students, 超过5名学生的课
-- Problem Url:  https://leetcode-cn.com/problems/classes-more-than-5-students/
-- Problem Level:  Easy
-- Language:  MySQL
 
# Write your MySQL query statement below
select class
from courses
group by class
having count(DISTINCT student) >= 5 