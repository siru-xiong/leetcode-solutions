# Problem Id:  674
# Problem Name:  Longest Continuous Increasing Subsequence, 最长连续递增序列
# Problem Url:  https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            vmax = 1
            left_index = 0
            for i in range(1,len(nums)):
                if nums[i] > nums[i-1]:
                    vmax = max(vmax,i-left_index+1)
                else:
                    left_index = i
            return vmax

