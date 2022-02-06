-- Problem Id:  1435
-- Problem Name:  Create a Session Bar Chart, 制作会话柱状图
-- Problem Url:  https://leetcode-cn.com/problems/create-a-session-bar-chart/
-- Problem Level:  Easy
-- Language:  MySQL
 
# Write your MySQL query statement below
select a.bin, case when b.total is null then 0 else b.total end as total from
(
select '[0-5>' as bin union select '[5-10>' as bin  union select '[10-15>' as bin
union select '15 or more' as bin
) a
left join
(
    select case when duration/60 >= 0 and duration/60 < 5 THEN '[0-5>'
when duration/60 >= 5 and duration/60 < 10 THEN '[5-10>'
when duration/60 >= 10 and duration/60 < 15 THEN '[10-15>'
when duration/60 >= 15 THEN '15 or more' end as bin, count(*) as TOTAL
from Sessions
group by bin
) b
on a.bin = b.bin