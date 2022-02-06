# Problem Id:  1779
# Problem Name:  Find Nearest Point That Has the Same X or Y Coordinate, 找到最近的有相同 X 或 Y 坐标的点
# Problem Url:  https://leetcode-cn.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        t = -1
        v = float('inf')
        for i in range(len(points)):
            if x == points[i][0] or y == points[i][1]:
                dist = abs(x - points[i][0]) + abs(y - points[i][1])
                if dist < v:
                    v = dist
                    t = i
        return t