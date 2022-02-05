# Problem Id:  78
# Problem Name:  Subsets, 子集
# Problem Url:  https://leetcode-cn.com/problems/subsets/
# Problem Level:  Medium
 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        else:
            mid = self.subsets(nums[1:])
            res = [[nums[0]]+i for i in mid] + mid
            return res
            