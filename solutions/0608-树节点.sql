-- Problem Id:  608
-- Problem Name:  Tree Node, 树节点
-- Problem Url:  https://leetcode-cn.com/problems/tree-node/
-- Problem Level:  Medium
-- Language:  MySQL
 
# Write your MySQL query statement below】
select t.id, t.type from
(
select s1.id, case when s2.id is not null and s1.p_id is not null then 'Inner' when s1.p_id is null then 'Root' else 'Leaf' end as type
from
tree s1
left join
tree s2
on s1.id = s2.p_id
) t
group by t.id