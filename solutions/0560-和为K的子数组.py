# Problem Id:  560
# Problem Name:  Subarray Sum Equals K, 和为 K 的子数组
# Problem Url:  https://leetcode-cn.com/problems/subarray-sum-equals-k/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ct = {}
        ct[0] = 1
        vsum = 0
        res = 0
        for i in range(len(nums)):
            vsum = vsum+nums[i]
            res = res + ct.get(vsum-k,0)
            ct[vsum]=ct.get(vsum,0)+1
        return res