# Problem Id:  597
# Problem Name:  Friend Requests I: Overall Acceptance Rate, 好友申请 I：总体通过率
# Problem Url:  https://leetcode-cn.com/problems/friend-requests-i-overall-acceptance-rate/
# Problem Level:  Easy
 
# Write your MySQL query statement below
select
ifnull(ROUND(
(select count(distinct requester_id,accepter_id) from
RequestAccepted)
/
(select count(distinct sender_id,send_to_id) from
FriendRequest),2),0) as accept_rate