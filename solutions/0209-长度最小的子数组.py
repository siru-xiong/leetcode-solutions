# Problem Id:  209
# Problem Name:  Minimum Size Subarray Sum, 长度最小的子数组
# Problem Url:  https://leetcode-cn.com/problems/minimum-size-subarray-sum/
# Problem Level:  Medium
 
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        s = 0
        l = float('inf')
        for i in range(len(nums)):
            s += nums[i]
            while s >= target:
                l = min(l,i-left+1)
                s -= nums[left]
                left += 1
        if l == float('inf'):
            return 0
        else:
            return l

