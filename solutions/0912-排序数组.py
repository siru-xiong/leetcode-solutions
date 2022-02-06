# Problem Id:  912
# Problem Name:  Sort an Array, 排序数组
# Problem Url:  https://leetcode-cn.com/problems/sort-an-array/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                nums[0],nums[1] = nums[1],nums[0]
            return nums
        else:
            ind = len(nums)//2
            left = self.sortArray(nums[:ind])
            right = self.sortArray(nums[ind:])
            return self.merge(left,right)

    def merge(self,n1,n2):
        res = []
        i = 0
        j = 0
        while i < len(n1) and j < len(n2):
            if n1[i] <= n2[j]:
                res.append(n1[i])
                i += 1
            else:
                res.append(n2[j])
                j += 1
        if i < len(n1):
            res = res + n1[i:]
        if j < len(n2):
            res = res + n2[j:]
        return res