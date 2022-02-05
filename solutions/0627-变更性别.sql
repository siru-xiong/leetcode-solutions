# Problem Id:  627
# Problem Name:  Swap Salary, 变更性别
# Problem Url:  https://leetcode-cn.com/problems/swap-salary/
# Problem Level:  Easy
 
# Write your MySQL query statement below
UPDATE salary 
SET sex = 
CASE
when sex = 'm' THEN 'f'
ELSE 'm'
END

#UPDATE salary 

#SET sex = if(sex = "m","f","m");