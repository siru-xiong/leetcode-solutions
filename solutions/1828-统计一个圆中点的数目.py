# Problem Id:  1828
# Problem Name:  Queries on Number of Points Inside a Circle, 统计一个圆中点的数目
# Problem Url:  https://leetcode-cn.com/problems/queries-on-number-of-points-inside-a-circle/
# Problem Level:  Medium
 
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = [0] * len(queries)
        for i in range(len(queries)):
            for j in range(len(points)):
                if (points[j][0]-queries[i][0])*(points[j][0]-queries[i][0])+(points[j][1]-queries[i][1])*(points[j][1]-queries[i][1]) <= queries[i][2]**2:
                    res[i] += 1
        return res