# Problem Id:  面试题 17.16
# Problem Name:  The Masseuse LCCI, 按摩师
# Problem Url:  https://leetcode-cn.com/problems/the-masseuse-lcci/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def massage(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            res = [nums[0],max(nums[1],nums[0])]
            for i in range(2,len(nums)):
                res.append(max(res[-1],res[-2]+nums[i]))
            return res[-1]