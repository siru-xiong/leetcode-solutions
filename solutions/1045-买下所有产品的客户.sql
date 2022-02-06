-- Problem Id:  1045
-- Problem Name:  Customers Who Bought All Products, 买下所有产品的客户
-- Problem Url:  https://leetcode-cn.com/problems/customers-who-bought-all-products/
-- Problem Level:  Medium
-- Language:  MySQL
 
# Write your MySQL query statement below
select customer_id from Customer
group by customer_id
having count(distinct(product_key)) =
(
    select count(distinct product_key) from Product
)