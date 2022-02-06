# Problem Id:  1413
# Problem Name:  Minimum Value to Get Positive Step by Step Sum, 逐步求和得到正数的最小值
# Problem Url:  https://leetcode-cn.com/problems/minimum-value-to-get-positive-step-by-step-sum/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        r = float('inf')
        t = 0
        for i in nums:
            t = t + i
            r = min(r,t)
        return max(1-r,1)