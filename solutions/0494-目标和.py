# Problem Id:  494
# Problem Name:  Target Sum, 目标和
# Problem Url:  https://leetcode-cn.com/problems/target-sum/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        vsum = sum(nums)
        if S > vsum:
            return 0
        else:
            S = vsum - S
            nums = [2*i for i in nums]
            res = [0] * (S+1)
            if nums[0] == 0:
                res[0] = 2
            else:
                res[0] = 1
                if nums[0] <= S:
                    res[nums[0]] = 1
            for j in range(1,len(nums)):
                for i in range(S,-1,-1):
                    if i >= nums[j]:
                        res[i] = res[i]+res[i-nums[j]]
            return res[S]
