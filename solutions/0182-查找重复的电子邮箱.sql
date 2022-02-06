-- Problem Id:  182
-- Problem Name:  Duplicate Emails, 查找重复的电子邮箱
-- Problem Url:  https://leetcode-cn.com/problems/duplicate-emails/
-- Problem Level:  Easy
-- Language:  MySQL
 
# Write your MySQL query statement below
select DISTINCT p1.Email from Person as p1
where 
(
    select count(*) from Person as p2 where p2.Email = p1.Email 
) > 1