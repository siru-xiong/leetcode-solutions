# Problem Id:  1237
# Problem Name:  Find Positive Integer Solution for a Given Equation, 找出给定方程的正整数解
# Problem Url:  https://leetcode-cn.com/problems/find-positive-integer-solution-for-a-given-equation/
# Problem Level:  Medium
 
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        start = [1,1000]
        while True:
            if start[1] <= 0 or start[0] <= 0 or start[1] > 1000 or start[0] > 1000:
                break
            if customfunction.f(start[0],start[1]) > z:
                start[1] -= 1
            elif customfunction.f(start[0],start[1]) < z:
                start[0] += 1
            else:
                res.append([start[0],start[1]])
                start[1] -= 1
                start[0] += 1
        return res