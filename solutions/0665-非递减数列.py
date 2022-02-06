# Problem Id:  665
# Problem Name:  Non-decreasing Array, 非递减数列
# Problem Url:  https://leetcode-cn.com/problems/non-decreasing-array/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        else:
            length = len(nums)
            nums = [float('-inf')] + nums + [float('inf')]
            true_count = 0
            count = 0
            for i in range(2,length+1):
                if nums[i] < nums[i-1]:
                    if nums[i-2] <= nums[i] or (i <= length and nums[i+1] >= nums[i-1]):
                        count = count + 1
                    else:
                        true_count = true_count + 1
            return true_count == 0 and count <= 1



