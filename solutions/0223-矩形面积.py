# Problem Id:  223
# Problem Name:  Rectangle Area, 矩形面积
# Problem Url:  https://leetcode-cn.com/problems/rectangle-area/
# Problem Level:  Medium
 
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        A = abs(ax1-ax2)*abs(ay1-ay2)
        B = abs(bx1-bx2)*abs(by1-by2)
        low = max(ay1,by1)
        high = min(ay2,by2)
        left = max(bx1,ax1)
        right = min(bx2,ax2)
        c = max(high-low,0) * max(right-left,0)
        return A+B-c

