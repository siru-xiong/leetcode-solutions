# Problem Id:  153
# Problem Name:  Find Minimum in Rotated Sorted Array, 寻找旋转排序数组中的最小值
# Problem Url:  https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
# Problem Level:  Medium
 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n=len(nums)
        left,right=0,n-1
        while left<= right:
            mid=left+(right-left)//2
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            elif nums[mid]<nums[right]:
                right=mid-1
            elif nums[mid]>nums[right]:
                left=mid+1