-- Problem Id:  607
-- Problem Name:  Sales Person, 销售员
-- Problem Url:  https://leetcode-cn.com/problems/sales-person/
-- Problem Level:  Easy
-- Language:  MySQL
 
# Write your MySQL query statement below
select name from salesperson where sales_id not in
(
select distinct sales_id from orders
inner join company
on company.com_id = orders.com_id  and company.name = 'RED'
)
