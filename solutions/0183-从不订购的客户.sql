# Problem Id:  183
# Problem Name:  Customers Who Never Order, 从不订购的客户
# Problem Url:  https://leetcode-cn.com/problems/customers-who-never-order/
# Problem Level:  Easy
 
# Write your MySQL query statement below
select c.Name as Customers from Customers as c
where c.Id not in (
    select O.CustomerId from Orders as o
)