-- Problem Id:  196
-- Problem Name:  Delete Duplicate Emails, 删除重复的电子邮箱
-- Problem Url:  https://leetcode-cn.com/problems/delete-duplicate-emails/
-- Problem Level:  Easy
-- Language:  MySQL
 
# Write your MySQL query statement below
DELETE FROM Person
where Id not in 
(
    select * from (select MIN(ID) From Person Group by Email) as t
)