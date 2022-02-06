# Problem Id:  33
# Problem Name:  Search in Rotated Sorted Array, 搜索旋转排序数组
# Problem Url:  https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        result = -1
        while right - left >= 2:
            mid = int((left + right)/2)
            if nums[mid] > nums[left]:
                if target < nums[left]:
                    left = mid
                else:
                    if target <= nums[mid]:
                        right = mid
                    else:
                        left = mid
            elif nums[mid] < nums[left]:
                if target >= nums[left]:
                    right = mid
                else:
                    if target <= nums[mid]:
                        right = mid
                    else:
                        left = mid
            else:
                result =  mid
                break
        if result == -1:
            if nums[left] == target:
                result = left
            elif nums[right] == target:
                result = right
        return result
        