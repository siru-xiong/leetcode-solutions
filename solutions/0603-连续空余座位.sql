-- Problem Id:  603
-- Problem Name:  Consecutive Available Seats, 连续空余座位
-- Problem Url:  https://leetcode-cn.com/problems/consecutive-available-seats/
-- Problem Level:  Easy
-- Language:  MySQL
 
# Write your MySQL query statement below
select distinct s1.seat_id from
(
    select seat_id from cinema where free = 1
) s1
inner join
(
    select seat_id from cinema where free = 1
) s2
on s1.seat_id = s2.seat_id - 1 or 
s1.seat_id = s2.seat_id + 1