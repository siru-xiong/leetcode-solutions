-- Problem Id:  197
-- Problem Name:  Rising Temperature, 上升的温度
-- Problem Url:  https://leetcode-cn.com/problems/rising-temperature/
-- Problem Level:  Easy
-- Language:  MySQL
 
# Write your MySQL query statement below
select w1.id
from Weather as w1, Weather as w2
where w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
and w1.temperature > w2.temperature