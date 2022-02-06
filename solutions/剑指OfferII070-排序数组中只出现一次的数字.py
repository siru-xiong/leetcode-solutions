# Problem Id:  剑指 Offer II 070
# Problem Name:  排序数组中只出现一次的数字, 排序数组中只出现一次的数字
# Problem Url:  https://leetcode-cn.com/problems/skFtm2/
# Problem Level:  Medium
# Language:  Python3
 
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

