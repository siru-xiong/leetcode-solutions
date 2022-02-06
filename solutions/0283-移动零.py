# Problem Id:  283
# Problem Name:  Move Zeroes, 移动零
# Problem Url:  https://leetcode-cn.com/problems/move-zeroes/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        j = 0
        while j < length + 1 and i < length:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                j = j + 1
            else:
                i = i + 1
            
