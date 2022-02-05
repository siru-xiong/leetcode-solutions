# Problem Id:  1050
# Problem Name:  Actors and Directors Who Cooperated At Least Three Times, 合作过至少三次的演员和导演
# Problem Url:  https://leetcode-cn.com/problems/actors-and-directors-who-cooperated-at-least-three-times/
# Problem Level:  Easy
 
# Write your MySQL query statement below
select actor_id, director_id from
ActorDirector
group by actor_id, director_id
having count(*) >= 3