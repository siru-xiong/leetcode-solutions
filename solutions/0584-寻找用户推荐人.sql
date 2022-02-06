-- Problem Id:  584
-- Problem Name:  Find Customer Referee, 寻找用户推荐人
-- Problem Url:  https://leetcode-cn.com/problems/find-customer-referee/
-- Problem Level:  Easy
-- Language:  MS SQL Server
 
/* Write your T-SQL query statement below */
select name from customer
where referee_id is Null or referee_id <> 2