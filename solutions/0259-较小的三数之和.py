# Problem Id:  259
# Problem Name:  3Sum Smaller, 较小的三数之和
# Problem Url:  https://leetcode-cn.com/problems/3sum-smaller/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)-2):
            res += self.check(nums[(i+1):],target-nums[i])
        return res
    
    def check(self,nums,target):
        i = 0 
        j = len(nums)-1
        res = 0
        while i < j:
            if nums[i]+nums[j] >= target:
                j = j -1
            else:
                res += j - i
                i += 1
        return res