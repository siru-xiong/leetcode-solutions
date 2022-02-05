# Problem Id:  47
# Problem Name:  Permutations II, 全排列 II
# Problem Url:  https://leetcode-cn.com/problems/permutations-ii/
# Problem Level:  Medium
 
class Solution:
    def per(self, nums: List[int]):
        if len(nums) == 1:
            return [[nums[0]]]
        else:
            curr = nums[0]
            re = []
            re = re + [[nums[0]]+j for j in self.per(nums[1:])]
            for i in range(1,len(nums)):
                if nums[i] != curr:
                    re = re + [[nums[i]] + j for j in self.per(nums[:i]+nums[(i+1):])]
                    curr = nums[i]
            return re

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.per(nums)