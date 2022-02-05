# Problem Id:  162
# Problem Name:  Find Peak Element, 寻找峰值
# Problem Url:  https://leetcode-cn.com/problems/find-peak-element/
# Problem Level:  Medium
 
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('-inf')]
        l = 1
        r = len(nums)-2
        while l < r-1:
            mid = (l+r) // 2
            if nums[mid] <= nums[mid+1]:
                l = mid
            elif nums[mid] <= nums[mid-1]:
                r = mid
            else:
                return mid-1
        if nums[l] > nums[l-1] and nums[l] > nums[l+1]:
            return l-1
        else:
            return r-1