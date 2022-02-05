# Problem Id:  剑指 Offer 57
# Problem Name:  和为s的两个数字 LCOF, 和为s的两个数字
# Problem Url:  https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/
# Problem Level:  Easy
 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                return [nums[i],nums[j]]