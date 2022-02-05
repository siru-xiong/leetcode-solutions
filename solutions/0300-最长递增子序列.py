# Problem Id:  300
# Problem Name:  Longest Increasing Subsequence, 最长递增子序列
# Problem Url:  https://leetcode-cn.com/problems/longest-increasing-subsequence/
# Problem Level:  Medium
 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] > d[-1]:
                d.append(nums[i])
            else:
                left = 0
                right = len(d)-1
                while right - left > 1:
                    mid = (right + left) // 2
                    if d[mid] < nums[i]:
                        left = mid
                    else:
                        right = mid
                if d[right] < nums[i]:
                    d[right+1] = min(d[right+1],nums[i])
                elif d[left] < nums[i]:
                    d[left+1] = min(d[left+1],nums[i])
                else:
                    d[left] = min(d[left],nums[i])
        print(d)
        return len(d)