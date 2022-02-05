# Problem Id:  剑指 Offer 62
# Problem Name:  圆圈中最后剩下的数字 LCOF, 圆圈中最后剩下的数字
# Problem Url:  https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/
# Problem Level:  Easy
 
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        res = 0
        i = 0
        while i < n:
            res = (m+res) % (i+1)
            i += 1
        return res