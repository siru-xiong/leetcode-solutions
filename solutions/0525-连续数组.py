# Problem Id:  525
# Problem Name:  Contiguous Array, 连续数组
# Problem Url:  https://leetcode-cn.com/problems/contiguous-array/
# Problem Level:  Medium
 
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        k = dict()
        k[0] = -1
        cummu = 0
        res = 0
        for i in range(len(nums)):
            cummu = cummu + nums[i]
            if cummu in k:
                res = max(res,i-k[cummu])
            else:
                k[cummu] = i
        return res

        