-- Problem Id:  619
-- Problem Name:  Biggest Single Number, 只出现一次的最大数字
-- Problem Url:  https://leetcode-cn.com/problems/biggest-single-number/
-- Problem Level:  Easy
-- Language:  MySQL
 
# Write your MySQL query statement below
select(
select num from my_numbers group by num having count(*) = 1 order by num desc limit 1
) num