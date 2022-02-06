-- Problem Id:  610
-- Problem Name:  Triangle Judgement, 判断三角形
-- Problem Url:  https://leetcode-cn.com/problems/triangle-judgement/
-- Problem Level:  Easy
-- Language:  MySQL
 
# Write your MySQL query statement below
select x,y,z, case when x+y>z and x+z>y and y+z>x then 'Yes' Else 'No' End as triangle from triangle