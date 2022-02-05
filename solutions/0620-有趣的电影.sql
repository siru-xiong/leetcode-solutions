# Problem Id:  620
# Problem Name:  Not Boring Movies, 有趣的电影
# Problem Url:  https://leetcode-cn.com/problems/not-boring-movies/
# Problem Level:  Easy
 
# Write your MySQL query statement below
select * from cinema
where description != 'boring'
and id % 2 = 1
order by rating DESC