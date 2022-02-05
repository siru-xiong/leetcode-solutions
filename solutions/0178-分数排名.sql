# Problem Id:  178
# Problem Name:  Rank Scores, 分数排名
# Problem Url:  https://leetcode-cn.com/problems/rank-scores/
# Problem Level:  Medium
 
# Write your MySQL query statement below
select s1.Score , count(distinct s2.Score) AS 'Rank' from
Scores as s1 , Scores as s2
where s1.score <= s2.score
group by s1.id
order by
s1.score DESC