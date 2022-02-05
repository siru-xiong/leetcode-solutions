# Problem Id:  812
# Problem Name:  Largest Triangle Area, 最大三角形面积
# Problem Url:  https://leetcode-cn.com/problems/largest-triangle-area/
# Problem Level:  Easy
 
class Solution:
    def area(p, q, r):
        return .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]-p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(p, q, r):
            return .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]-p[1]*q[0]-q[1]*r[0]-r[1]*p[0])
        x = len(points)
        res = 0
        for i in range(x-2):
            for j in range(i+1,x-1):
                for k in range(j+1,x):
                    res = max(res,area(points[i],points[j],points[k]))
        return res