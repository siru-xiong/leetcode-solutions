# Problem Id:  469
# Problem Name:  Convex Polygon, 凸多边形
# Problem Url:  https://leetcode-cn.com/problems/convex-polygon/
# Problem Level:  Medium
 
class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        sign = []
        for i in range(-2, len(points) - 2):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            x3, y3 = points[i + 2]
            det = lambda a, b, c, d: a * d - b * c
            p = det(x2 - x1, y2 - y1, x3 - x2, y3 - y2)
            if p > 0: sign.append(True)
            if p < 0: sign.append(False)
        return all(sign) == any(sign)