-- Problem Id:  1068
-- Problem Name:  Product Sales Analysis I, 产品销售分析 I
-- Problem Url:  https://leetcode-cn.com/problems/product-sales-analysis-i/
-- Problem Level:  Easy
-- Language:  MySQL
 
# Write your MySQL query statement below
select product_name,year,price
from Sales left join Product
on Sales.product_id=Product.product_id