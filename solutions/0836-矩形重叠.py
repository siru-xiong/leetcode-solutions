# Problem Id:  836
# Problem Name:  Rectangle Overlap, 矩形重叠
# Problem Url:  https://leetcode-cn.com/problems/rectangle-overlap/
# Problem Level:  Easy
 
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        s = False
        if rec1[0] < rec2[0] and rec2[0] < rec1[2] and rec2[0] < rec2[2]:
            s = True
        if rec1[0] == rec2[0] and min(rec1[2],rec2[2]) > rec1[0]:
            s = True
        if rec1[0] > rec2[0] and rec2[2] > rec1[0] and rec1[2] > rec1[0]:
            s = True
        t = False
        if rec1[1] < rec2[1] and rec2[1] < rec1[3] and rec2[1] < rec2[3]:
            t = True
        if rec1[1] == rec2[1] and min(rec1[3],rec2[3]) > rec1[1]:
            t = True
        if rec1[1] > rec2[1] and rec2[3] > rec1[1] and rec1[3] > rec1[1]:
            t = True
        return s and t