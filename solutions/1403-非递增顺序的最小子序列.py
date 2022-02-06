# Problem Id:  1403
# Problem Name:  Minimum Subsequence in Non-Increasing Order, 非递增顺序的最小子序列
# Problem Url:  https://leetcode-cn.com/problems/minimum-subsequence-in-non-increasing-order/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        vsum = sum(nums) / 2
        i = 0
        nsum = 0
        while nsum <= vsum:
            nsum = nsum + nums[i]
            i = i + 1
        return nums[:i]
