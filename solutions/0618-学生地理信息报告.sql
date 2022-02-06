-- Problem Id:  618
-- Problem Name:  Students Report By Geography, 学生地理信息报告
-- Problem Url:  https://leetcode-cn.com/problems/students-report-by-geography/
-- Problem Level:  Hard
-- Language:  MySQL
 
# Write your MySQL query statement below
select t1.name as America, t2.name as Asia, t3.name as Europe from 
(
    select name, row_number() over (order by name) as row_num
    from student where continent = 'America'
    order by name
) t1
left join
(
    select name,row_number() over (order by name) as row_num
     from student where continent = 'Asia'
     order by name
) t2
on t1.row_num = t2.row_num
left join
(
    select name,row_number() over (order by name) as row_num
    from student where continent = 'Europe'
    order by name
) t3
on t2.row_num = t3.row_num or t1.row_num = t3.row_num