# Problem Id:  剑指 Offer 42
# Problem Name:  连续子数组的最大和  LCOF, 连续子数组的最大和
# Problem Url:  https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
# Problem Level:  Easy
 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0 for _ in range(len(nums))]
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            if dp[i-1]>0:
                dp[i]=dp[i-1]+nums[i]
            else:
                dp[i]=nums[i]
        return max(dp)