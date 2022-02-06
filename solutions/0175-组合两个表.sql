-- Problem Id:  175
-- Problem Name:  Combine Two Tables, 组合两个表
-- Problem Url:  https://leetcode-cn.com/problems/combine-two-tables/
-- Problem Level:  Easy
-- Language:  MySQL
 
# Write your MySQL query statement below
select p.FirstName,p.LastName,a.City,a.State from
Person as p
left join
Address as a
on p.PersonId = a.PersonId