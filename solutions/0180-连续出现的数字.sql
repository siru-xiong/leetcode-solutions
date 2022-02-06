-- Problem Id:  180
-- Problem Name:  Consecutive Numbers, 连续出现的数字
-- Problem Url:  https://leetcode-cn.com/problems/consecutive-numbers/
-- Problem Level:  Medium
-- Language:  MySQL
 
# Write your MySQL query statement below
select DISTINCT(l1.Num) as ConsecutiveNums
from
Logs as l1,Logs as l2,Logs as l3
where
l2.Id = l1.Id + 1
and 
l3.Id = l2.Id + 1
and
l1.Num = l2.Num
and
l2.Num = l3.Num