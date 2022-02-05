# Problem Id:  595
# Problem Name:  Big Countries, 大的国家
# Problem Url:  https://leetcode-cn.com/problems/big-countries/
# Problem Level:  Easy
 
# Write your MySQL query statement below
select name, population ,area
from world
where area > 3000000
or population > 25000000