# Problem Id:  1393
# Problem Name:  Capital Gain/Loss, 股票的资本损益
# Problem Url:  https://leetcode-cn.com/problems/capital-gainloss/
# Problem Level:  Medium
 
# Write your MySQL query statement below
select stock_name, sum(case when operation = 'Buy' then -price else price end) as capital_gain_loss
from Stocks
group by stock_name