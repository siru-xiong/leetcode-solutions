-- Problem Id:  262
-- Problem Name:  Trips and Users, 行程和用户
-- Problem Url:  https://leetcode-cn.com/problems/trips-and-users/
-- Problem Level:  Hard
-- Language:  MySQL
 
# Write your MySQL query statement below
select DISTINCT(t2.Request_at) as Day,
(
select ROUND(SUM(temp)/count(*),2) from (
select CASE
WHEN Status != 'completed' THEN 1 
ELSE 0 END AS temp
 from Trips as t
where t.Client_Id in
(select u1.Users_Id from Users as u1 where u1.banned = 'No' and u1.Role = 'client')
and  t.Driver_Id in 
(select u2.Users_Id from Users as u2 where u2.banned = 'No' and u2.Role = 'driver')
and t.Request_at = t2.Request_at
) as q
) as 'Cancellation Rate'
from Trips as t2
where t2.Request_at BETWEEN '2013-10-01' AND '2013-10-03'