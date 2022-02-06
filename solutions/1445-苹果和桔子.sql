-- Problem Id:  1445
-- Problem Name:  Apples & Oranges, 苹果和桔子
-- Problem Url:  https://leetcode-cn.com/problems/apples-oranges/
-- Problem Level:  Medium
-- Language:  MySQL
 
# Write your MySQL query statement below
select sale_date, SUM(case when fruit='apples' then sold_num else -sold_num end) as diff
from Sales
group by sale_date
order by sale_date