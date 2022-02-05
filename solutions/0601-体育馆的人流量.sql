# Problem Id:  601
# Problem Name:  Human Traffic of Stadium, 体育馆的人流量
# Problem Url:  https://leetcode-cn.com/problems/human-traffic-of-stadium/
# Problem Level:  Hard
 
# Write your MySQL query statement below
select distinct a.*
from Stadium as a , Stadium as b , Stadium as c
where a.people >= 100 and b.people >= 100 and c.people >= 100
and (
 (a.id = b.id-1 and b.id = c.id -1 ) or (a.id = b.id -1 and a.id = c.id + 1) or
 (a.id = b.id+1 and b.id = c.id+ 1)
)
order by a.id