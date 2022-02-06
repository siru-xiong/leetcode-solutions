-- Problem Id:  1070
-- Problem Name:  Product Sales Analysis III, 产品销售分析 III
-- Problem Url:  https://leetcode-cn.com/problems/product-sales-analysis-iii/
-- Problem Level:  Medium
-- Language:  MySQL
 
# Write your MySQL query statement below
select product_id, year as first_year, quantity, price
from (
select * , rank() over (partition by product_id order by year) r
from Sales
) t
where r = 1