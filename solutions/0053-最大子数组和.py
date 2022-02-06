# Problem Id:  53
# Problem Name:  Maximum Subarray, 最大子数组和
# Problem Url:  https://leetcode-cn.com/problems/maximum-subarray/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        save = [nums[0]]
        vmax = save[0]
        for i in range(1,len(nums)):
            save = save + [max(save[i-1]+nums[i],nums[i])]
            if save[i] > vmax:
                vmax = save[i]
        return vmax
