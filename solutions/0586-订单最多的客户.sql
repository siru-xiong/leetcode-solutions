# Problem Id:  586
# Problem Name:  Customer Placing the Largest Number of Orders, 订单最多的客户
# Problem Url:  https://leetcode-cn.com/problems/customer-placing-the-largest-number-of-orders/
# Problem Level:  Easy
 
# Write your MySQL query statement below
select customer_number
from orders
group by customer_number
order by count(*) desc
limit 1