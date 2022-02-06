# Problem Id:  492
# Problem Name:  Construct the Rectangle, 构造矩形
# Problem Url:  https://leetcode-cn.com/problems/construct-the-rectangle/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        import math
        q = int(math.sqrt(area))
        for i in range(q,0,-1):
            if area % i == 0:
                return [area // i , i]
                break