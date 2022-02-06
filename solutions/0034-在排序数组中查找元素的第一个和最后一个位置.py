# Problem Id:  34
# Problem Name:  Find First and Last Position of Element in Sorted Array, 在排序数组中查找元素的第一个和最后一个位置
# Problem Url:  https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        left = -1
        right = -1
        li = 0
        ri = len(nums)-1
        while ri-li >1:
            med = int((ri + li)/2)
            if nums[med] < target:
                li = med + 1
            elif nums[med] >= target:
                ri = med
        if nums[li] == target:
            left = li
        elif nums[ri] == target:
            left = ri

        li = 0
        ri = len(nums)-1
        while ri-li >1:
            med = int((ri + li)/2)
            if nums[med] <= target:
                li = med
            elif nums[med] > target:
                ri = med - 1
        if nums[ri] == target:
            right = ri
        elif nums[li] == target:
            right = li
        
        return [left,right]

        
        