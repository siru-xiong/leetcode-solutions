# Problem Id:  剑指 Offer II 012
# Problem Name:  左右两边子数组的和相等, 左右两边子数组的和相等
# Problem Url:  https://leetcode-cn.com/problems/tvdfij/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0
        else:
            left = 0
            right = sum(nums[1:])
            for i in range(len(nums)-1):
                if left == right:
                    return i
                else:
                    left += nums[i]
                    right -= nums[i+1]
            if left == right:
                return len(nums)-1
            else:
                return -1
