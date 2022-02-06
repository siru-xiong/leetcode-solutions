# Problem Id:  1480
# Problem Name:  Running Sum of 1d Array, 一维数组的动态和
# Problem Url:  https://leetcode-cn.com/problems/running-sum-of-1d-array/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums