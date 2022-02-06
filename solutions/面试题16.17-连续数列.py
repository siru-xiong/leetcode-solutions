# Problem Id:  面试题 16.17
# Problem Name:  Contiguous Sequence LCCI, 连续数列
# Problem Url:  https://leetcode-cn.com/problems/contiguous-sequence-lcci/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(nums[0])
            else:
                res.append(max(nums[i],res[-1]+nums[i]))
        return max(res)