# Problem Id:  31
# Problem Name:  Next Permutation, 下一个排列
# Problem Url:  https://leetcode-cn.com/problems/next-permutation/
# Problem Level:  Medium
 
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                index = 1
                temp = i - 1
                break
        if index == 1:
            for j in range(len(nums)-1,temp,-1):
                if nums[j] > nums[temp]:
                    nums[j],nums[temp] = nums[temp],nums[j]
                    break
            nums[(temp+1):] = nums[(temp+1):][::-1]
            return nums
        else:
            nums[:] = nums[:][::-1]
            return nums