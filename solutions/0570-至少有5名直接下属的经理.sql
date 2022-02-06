-- Problem Id:  570
-- Problem Name:  Managers with at Least 5 Direct Reports, 至少有5名直接下属的经理
-- Problem Url:  https://leetcode-cn.com/problems/managers-with-at-least-5-direct-reports/
-- Problem Level:  Medium
-- Language:  MySQL
 
# Write your MySQL query statement below
select e1.Name from Employee as e1 where e1.Id in
(
select e2.ManagerId from Employee as e2
group by e2.ManagerId
having count(*) >= 5
)