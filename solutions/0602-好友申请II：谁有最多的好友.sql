-- Problem Id:  602
-- Problem Name:  Friend Requests II: Who Has the Most Friends, 好友申请 II ：谁有最多的好友
-- Problem Url:  https://leetcode-cn.com/problems/friend-requests-ii-who-has-the-most-friends/
-- Problem Level:  Medium
-- Language:  MySQL
 
# Write your MySQL query statement below
select distinct id,
(
select count(distinct uid) from (
select  accepter_id as uid from request_accepted
where requester_id = all_id.id
union
select requester_id as uid from request_accepted
where accepter_id = all_id.id
) a1 ) as num

from
(
    select requester_id as id from request_accepted
    union 
    select accepter_id  as id from request_accepted
) all_id
order by num desc
limit 1
