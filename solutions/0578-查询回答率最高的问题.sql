-- Problem Id:  578
-- Problem Name:  Get Highest Answer Rate Question, 查询回答率最高的问题
-- Problem Url:  https://leetcode-cn.com/problems/get-highest-answer-rate-question/
-- Problem Level:  Medium
-- Language:  MySQL
 
# Write your MySQL query statement below
select t1.question_id as survey_log
from 
(
select question_id,count(*) as c from survey_log
where action = 'show'
group by question_id ) t1
inner join
(
select question_id,count(*) as c from survey_log
where action = 'answer'
group by question_id
) t2
on t1.question_id = t2.question_id
order by t2.c/t1.c desc
limit 1