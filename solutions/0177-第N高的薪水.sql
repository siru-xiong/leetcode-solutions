# Problem Id:  177
# Problem Name:  Nth Highest Salary, 第N高的薪水
# Problem Url:  https://leetcode-cn.com/problems/nth-highest-salary/
# Problem Level:  Medium
 
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
 SET N = N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT IFNULL((select distinct Salary from Employee order by Salary DESC LIMIT N,1),NULL) AS getNthHighestSalary
  );
END