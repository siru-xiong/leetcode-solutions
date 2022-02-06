# Problem Id:  356
# Problem Name:  Line Reflection, 直线镜像
# Problem Url:  https://leetcode-cn.com/problems/line-reflection/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if points == []:
            return True
        points = set([tuple(i) for i in points])
        left = min([i[0] for i in points])
        right = max([i[0] for i in points])
        mid = (left+right)/2
        for i in points:
            if (2*mid - i[0],i[1]) not in points:
                return False
        return True
