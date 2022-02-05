# Problem Id:  594
# Problem Name:  Longest Harmonious Subsequence, 最长和谐子序列
# Problem Url:  https://leetcode-cn.com/problems/longest-harmonious-subsequence/
# Problem Level:  Easy
 
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}
        #nums.sort()
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0) + 1
        result = 0
        for i in range(len(nums)):
            if nums[i]-1 in count and count[nums[i]]+count[nums[i]-1] > result:
                result = count[nums[i]]+count[nums[i]-1]
            if nums[i]+1 in count and count[nums[i]]+count[nums[i]+1] > result:
                result = count[nums[i]]+count[nums[i]+1]
        return result
        #value = list(count.values())
        #key = list(count.keys())
        #if len(count) <= 1:
        #    return 0
        #else:
        #    result = 0
        #    for i in range(0,len(count)-1):
        #        if value[i]+value[i+1] > result and key[i+1]-key[i] == 1:
        #            result = value[i]+value[i+1]
        #    return result
