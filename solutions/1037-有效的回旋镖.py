# Problem Id:  1037
# Problem Name:  Valid Boomerang, 有效的回旋镖
# Problem Url:  https://leetcode-cn.com/problems/valid-boomerang/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if len(set(map(tuple,points))) !=3:
            return False
        elif points[0][0] == points[1][0]:
            return points[2][0] != points[1][0]
        elif points[1][0] == points[2][0]:
            return points[0][0] != points[1][0]
        else:
            return (points[1][1]-points[0][1])/(points[1][0]-points[0][0]) != (points[2][1]-points[1][1])/(points[2][0]-points[1][0])