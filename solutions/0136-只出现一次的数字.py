# Problem Id:  136
# Problem Name:  Single Number, 只出现一次的数字
# Problem Url:  https://leetcode-cn.com/problems/single-number/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        return res