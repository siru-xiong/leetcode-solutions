# Problem Id:  1725
# Problem Name:  Number Of Rectangles That Can Form The Largest Square, 可以形成最大正方形的矩形数目
# Problem Url:  https://leetcode-cn.com/problems/number-of-rectangles-that-can-form-the-largest-square/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        temp = [min(i) for i in rectangles]
        vmax = max(temp)
        count = 0
        for i in temp:
            if i == vmax:
                count = count + 1
        return count