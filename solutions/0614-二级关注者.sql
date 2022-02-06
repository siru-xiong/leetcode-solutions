-- Problem Id:  614
-- Problem Name:  Second Degree Follower, 二级关注者
-- Problem Url:  https://leetcode-cn.com/problems/second-degree-follower/
-- Problem Level:  Medium
-- Language:  MySQL
 
# Write your MySQL query statement below
select s1.follower, count(distinct s2.follower) as num
from follow s1
inner join follow s2
on s1.follower = s2.followee
group by
s1.follower
order by s1.follower