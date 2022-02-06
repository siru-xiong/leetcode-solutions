-- Problem Id:  571
-- Problem Name:  Find Median Given Frequency of Numbers, 给定数字的频率查询中位数
-- Problem Url:  https://leetcode-cn.com/problems/find-median-given-frequency-of-numbers/
-- Problem Level:  Hard
-- Language:  MySQL
 
# Write your MySQL query statement below
select round(avg(t.number),4) as median
from (
select
number,
sum(frequency) over (order by number) as t1,
sum(frequency) over (order by number desc) as t2
from 
numbers
order by number
) t

where t.t1 >= (select sum(frequency)/2 from numbers)
and t.t2 >=  (select sum(frequency)/2 from numbers)