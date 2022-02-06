# Problem Id:  75
# Problem Name:  Sort Colors, 颜色分类
# Problem Url:  https://leetcode-cn.com/problems/sort-colors/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)-1
        k = 0
        while True:
            while i < len(nums) and nums[i] == 0:
                i = i + 1
            while j >=0 and nums[j] == 2:
                j = j - 1
            k = max(k,i)
            if k > j:
                break
            if nums[k] == 2:
                nums[k],nums[j] = nums[j],nums[k]
            if nums[k] == 0:
                nums[k],nums[i] = nums[i],nums[k]
            k = k + 1
