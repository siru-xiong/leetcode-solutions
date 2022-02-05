# Problem Id:  704
# Problem Name:  Binary Search, 二分查找
# Problem Url:  https://leetcode-cn.com/problems/binary-search/
# Problem Level:  Easy
 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while right-left >= 2:
            med = int((left+right)/2)
            if nums[med] > target:
                right = med
            elif nums[med] < target:
                left = med
            else:
                right = med
                left = med
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1