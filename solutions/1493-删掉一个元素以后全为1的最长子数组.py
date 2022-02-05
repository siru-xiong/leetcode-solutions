# Problem Id:  1493
# Problem Name:  Longest Subarray of 1's After Deleting One Element, 删掉一个元素以后全为 1 的最长子数组
# Problem Url:  https://leetcode-cn.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# Problem Level:  Medium
 
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums) == len(nums):
            return len(nums)-1
        if sum(nums) == 0:
            return 0
        res = []
        k = 1
        start = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == start:
                k += 1
            else:
                if nums[i] == 0:
                    res.append('1'+str(k))
                    k = 1
                    start = nums[i]
                else:
                    res.append('0'+str(k))
                    k = 1
                    start = nums[i]
        res.append(str(start)+str(k))
        r = 0
        for i in range(len(res)):
            if res[i][0] == '0':
                if res[i][1:] == '1':
                    if i > 0 and i < len(res)-1:
                        r = max(r,int(res[i-1][1:])+int(res[i+1][1:]))
                    elif i == 0:
                        r = max(r,int(res[i+1][1:]))
                    else:
                        r = max(r,int(res[i-1][1:]))
                else:
                    if i > 0 and i < len(res)-1:
                        r = max(r,max(int(res[i-1][1:]),int(res[i+1][1:])))
                    elif i == 0:
                        r = max(r,int(res[i+1][1:]))
                    else:
                        r = max(r,int(res[i-1][1:]))
        return r