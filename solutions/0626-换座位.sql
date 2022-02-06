-- Problem Id:  626
-- Problem Name:  Exchange Seats, 换座位
-- Problem Url:  https://leetcode-cn.com/problems/exchange-seats/
-- Problem Level:  Medium
-- Language:  MySQL
 
# Write your MySQL query statement below
select s1.id , s2.student
from seat as s1, seat as s2
where
(s1.id % 2 = 1 and s1.id = (select max(s.id) from seat as s) and s1.id = s2.id)
or
(
    s1.id % 2 = 1 and s1.id = s2.id - 1
)
or
(
    s1.id % 2 = 0 and s1.id = s2.id + 1
)
order by s1.id