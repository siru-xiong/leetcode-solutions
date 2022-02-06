# Problem Id:  154
# Problem Name:  Find Minimum in Rotated Sorted Array II, 寻找旋转排序数组中的最小值 II
# Problem Url:  https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
# Problem Level:  Hard
# Language:  Python3
 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return min(nums)
        else:
            l = 0
            r = len(nums) - 1
            mid = (l+r) // 2
            if nums[mid] >= nums[l] and nums[r] >= nums[mid] and nums[l] != nums[r]:
                return nums[l]
            elif nums[mid] == nums[l] and nums[mid] == nums[r]:
                return min(self.findMin(nums[:(mid+1)]),self.findMin(nums[mid:]))
            elif nums[mid] <= nums[l] and nums[mid] <= nums[r]:
                return self.findMin(nums[:(mid+1)])
            else:
                return self.findMin(nums[mid:])