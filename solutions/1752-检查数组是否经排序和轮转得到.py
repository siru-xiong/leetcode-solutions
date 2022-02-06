# Problem Id:  1752
# Problem Name:  Check if Array Is Sorted and Rotated, 检查数组是否经排序和轮转得到
# Problem Url:  https://leetcode-cn.com/problems/check-if-array-is-sorted-and-rotated/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def check(self, nums: List[int]) -> bool:
        vm = min(nums)
        if nums[0] == vm:
            index = 0
            for k in range(len(nums)):
                if nums[k] == vm:
                    tp = k
                else:
                    break
            for j in range(len(nums)-1,tp,-1):
                if nums[j] == vm:
                    index = j
            nums = nums[index:] + nums[:index]
        else:
            for i in range(len(nums)):
                if nums[i] == vm:
                    index = i
                    break
            nums = nums[index:] + nums[:index]
        t = True
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                t = False
                break
        return t
