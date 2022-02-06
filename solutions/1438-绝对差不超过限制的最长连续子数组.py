# Problem Id:  1438
# Problem Name:  Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit, 绝对差不超过限制的最长连续子数组
# Problem Url:  https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        nn = []
        nq = []
        i = 1
        start = nums[0]
        for index in range(1,len(nums)):
            if nums[index] == start:
                i = i + 1
            else:
                nq.append(start)
                nn.append(i)
                start = nums[index]
                i = 1
        nq.append(start)
        nn.append(i)
        nums = nq
        minq = []
        maxq = []
        l = 0
        r = 0
        ans = 0
        while r < len(nums):
            while len(minq) > 0 and nums[r] < minq[-1]:
                del minq[-1]
            minq.append(nums[r])
            while len(maxq) > 0 and nums[r] > maxq[-1]:
                del maxq[-1]
            maxq.append(nums[r])
            r = r + 1
            while abs(maxq[0]-minq[0]) > limit:
                if maxq[0] == nums[l]:
                    del maxq[0]
                if minq[0] == nums[l]:
                    del minq[0]
                l = l + 1
            ans = max(ans,sum(nn[l:r]))
        return ans