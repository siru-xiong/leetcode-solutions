-- Problem Id:  1069
-- Problem Name:  Product Sales Analysis II, 产品销售分析 II
-- Problem Url:  https://leetcode-cn.com/problems/product-sales-analysis-ii/
-- Problem Level:  Easy
-- Language:  MySQL
 
# Write your MySQL query statement below
select Sales.product_id, sum(quantity) as total_quantity
from Sales left join Product
on Sales.product_id=Product.product_id
group by Sales.product_id