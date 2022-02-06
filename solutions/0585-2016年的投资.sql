-- Problem Id:  585
-- Problem Name:  Investments in 2016, 2016年的投资
-- Problem Url:  https://leetcode-cn.com/problems/investments-in-2016/
-- Problem Level:  Medium
-- Language:  MySQL
 
# Write your MySQL query statement below
select sum(tiv_2016) as tiv_2016 from insurance
where tiv_2015 in
(
    select tiv_2015 from insurance
    group by tiv_2015
    having count(*) >= 2
)
and (lat,lon) in
(
    select lat,lon from insurance
    group by lat,lon
    having count(*) = 1
)