# Problem Id:  面试题 17.04
# Problem Name:  Missing Number LCCI, 消失的数字
# Problem Url:  https://leetcode-cn.com/problems/missing-number-lcci/
# Problem Level:  Easy
 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        res ^= len(nums)
        return res
