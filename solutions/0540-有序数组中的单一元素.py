# Problem Id:  540
# Problem Name:  Single Element in a Sorted Array, 有序数组中的单一元素
# Problem Url:  https://leetcode-cn.com/problems/single-element-in-a-sorted-array/
# Problem Level:  Medium
 
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            left = 0
            right = len(nums)-1
            while left < right - 1:
                mid = (left+right) // 2
                if mid % 2 == 0 and nums[mid] == nums[mid-1]:
                    right = mid
                elif mid % 2 == 1 and nums[mid] == nums[mid-1]:
                    left = mid + 1
                elif mid % 2 == 0 and nums[mid] != nums[mid-1]:
                    left = mid
                else:
                    right = mid - 1
            return nums[left]