# Problem Id:  剑指 Offer 53 - II
# Problem Name:  缺失的数字  LCOF, 0～n-1中缺失的数字
# Problem Url:  https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid
        print(left,right)
        if nums[left] == left:
            if nums[right] == right:
                return right + 1
            else:
                return right
        else:
            return left