# Problem Id:  377
# Problem Name:  Combination Sum IV, 组合总和 Ⅳ
# Problem Url:  https://leetcode-cn.com/problems/combination-sum-iv/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = [0] * (target+1)
        res[0] = 1
        for i in range(target+1):
            for j in range(len(nums)):
                if i - nums[j] >= 0:
                    res[i] = res[i] + res[i-nums[j]]
        return res[-1]