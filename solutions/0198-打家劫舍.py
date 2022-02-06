# Problem Id:  198
# Problem Name:  House Robber, 打家劫舍
# Problem Url:  https://leetcode-cn.com/problems/house-robber/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            save = [nums[0],max(nums[0:2])]
            for i in range(2,len(nums)):
                save = save + [max(save[i-2]+nums[i],save[i-1])]
            return save[len(nums)-1]