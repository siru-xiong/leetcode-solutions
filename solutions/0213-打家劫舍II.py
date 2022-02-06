# Problem Id:  213
# Problem Name:  House Robber II, 打家劫舍 II
# Problem Url:  https://leetcode-cn.com/problems/house-robber-ii/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        elif len(nums) == 3:
            return max(nums)
        else:
            res = [nums[0],nums[1],nums[0]+nums[2]]
            for i in range(3,len(nums)-1):
                res.append(max(res[:(-1)])+nums[i])
            a = max(res)
            nums = nums[1:]
            res = [nums[0],nums[1],nums[0]+nums[2]]
            for i in range(3,len(nums)):
                res.append(max(res[:(-1)])+nums[i])
            b = max(res)
            return max(a,b)