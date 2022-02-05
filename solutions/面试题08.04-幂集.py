# Problem Id:  面试题 08.04
# Problem Name:  Power Set LCCI, 幂集
# Problem Url:  https://leetcode-cn.com/problems/power-set-lcci/
# Problem Level:  Medium
 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        elif len(nums) == 1:
            return [[],[nums[0]]]
        else:
            a = self.subsets(nums[1:])
            return a + [[nums[0]]+i for i in a]