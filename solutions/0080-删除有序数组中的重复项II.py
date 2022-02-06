# Problem Id:  80
# Problem Name:  Remove Duplicates from Sorted Array II, 删除有序数组中的重复项 II
# Problem Url:  https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        last = float('-inf')
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                if nums[i] != last:
                    nums[index] = nums[i]
                    nums[index+1] = nums[i]
                    last = nums[i]
                    index = index + 2
                i = i + 2
            else:               
                if nums[i] != last:
                    nums[index] = nums[i]
                    last = nums[i]
                    index = index + 1
                i = i + 1
        if i <= len(nums)-1 and nums[i] != last:
            nums[index] = nums[i]
            index = index + 1
        return index
