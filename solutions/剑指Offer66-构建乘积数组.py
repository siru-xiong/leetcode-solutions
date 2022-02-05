# Problem Id:  剑指 Offer 66
# Problem Name:  构建乘积数组 LCOF, 构建乘积数组
# Problem Url:  https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/
# Problem Level:  Medium
 
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        res = [1] * len(a)
        start = 1
        end = 1
        for i in range(len(a)):
            res[i] *= start
            start *= a[i]
            res[-(i+1)] *= end
            end *= a[-(i+1)]
        return res