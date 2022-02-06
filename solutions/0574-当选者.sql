-- Problem Id:  574
-- Problem Name:  Winning Candidate, 当选者
-- Problem Url:  https://leetcode-cn.com/problems/winning-candidate/
-- Problem Level:  Medium
-- Language:  MySQL
 
# Write your MySQL query statement below
select name from Candidate
inner join (
select CandidateId,count(*) from vote
group by CandidateId
order by count(*) desc
limit 1 ) t
on t.CandidateId = candidate.id