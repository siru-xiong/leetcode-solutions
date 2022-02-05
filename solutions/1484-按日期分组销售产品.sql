# Problem Id:  1484
# Problem Name:  Group Sold Products By The Date, 按日期分组销售产品
# Problem Url:  https://leetcode-cn.com/problems/group-sold-products-by-the-date/
# Problem Level:  Easy
 
# Write your MySQL query statement below
select 
sell_date,count(distinct product)  as num_sold ,GROUP_CONCAT(distinct product order by product SEPARATOR ',') products  
from 
Activities 
group by
sell_date  
order by
sell_date  