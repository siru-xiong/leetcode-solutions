-- Problem Id:  613
-- Problem Name:  Shortest Distance in a Line, 直线上的最近距离
-- Problem Url:  https://leetcode-cn.com/problems/shortest-distance-in-a-line/
-- Problem Level:  Easy
-- Language:  MySQL
 
# Write your MySQL query statement below
select min(abs(a.x-b.x)) as shortest
from
point a
inner join
point b
on a.x != b.x