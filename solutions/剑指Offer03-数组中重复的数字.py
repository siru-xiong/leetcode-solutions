# Problem Id:  剑指 Offer 03
# Problem Name:  数组中重复的数字 LCOF, 数组中重复的数字
# Problem Url:  https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
# Problem Level:  Easy
 
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        ct = {}
        for i in nums:
            if i in ct:
                return i
            else:
                ct[i] = 0