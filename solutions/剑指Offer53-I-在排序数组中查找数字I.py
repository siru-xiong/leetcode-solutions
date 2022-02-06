# Problem Id:  剑指 Offer 53 - I
# Problem Name:  在排序数组中查找数字  LCOF, 在排序数组中查找数字 I
# Problem Url:  https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        l = 0
        r = len(nums)-1
        while r-l >1:
            mid = (l+r) // 2
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid
            else:
                if nums[l] < target:
                    l += 1
                elif nums[r] > target:
                    r -= 1
                else:
                    return r -l + 1
        if r==l:
            if nums[r] == target:
                return 1
            else:
                return 0
        elif l == r - 1:
            res = 0
            if nums[r] == target:
                res += 1
            if nums[l] == target:
                res += 1
            return res
        return 0
