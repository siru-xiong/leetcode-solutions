# Problem Id:  46
# Problem Name:  Permutations, 全排列
# Problem Url:  https://leetcode-cn.com/problems/permutations/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            res = []
            for i in range(len(nums)):
                t = self.permute(nums[:i]+nums[(i+1):])
                res += [[nums[i]]+u for u in t]
            return res