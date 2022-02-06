# Problem Id:  485
# Problem Name:  Max Consecutive Ones, 最大连续 1 的个数
# Problem Url:  https://leetcode-cn.com/problems/max-consecutive-ones/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxcount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count = count + 1
            else:
                maxcount = max(maxcount,count)
                count = 0
        maxcount = max(maxcount,count)
        return maxcount