# Problem Id:  128
# Problem Name:  Longest Consecutive Sequence, 最长连续序列
# Problem Url:  https://leetcode-cn.com/problems/longest-consecutive-sequence/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for i in nums:
            if i - 1 not in nums:
                s = i
                t = 1
                while s + 1 in nums:
                    s += 1
                    t += 1
                res = max(res,t)
        return res