# Problem Id:  612
# Problem Name:  Shortest Distance in a Plane, 平面上的最近距离
# Problem Url:  https://leetcode-cn.com/problems/shortest-distance-in-a-plane/
# Problem Level:  Medium
 
# Write your MySQL query statement below
select MIN(ROUND( SQRT((a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y)),2)) as shortest
from point_2d a
inner join
point_2d b
on a.x != b.x or a.y != b.y