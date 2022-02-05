# Problem Id:  剑指 Offer II 083
# Problem Name:  没有重复元素集合的全排列, 没有重复元素集合的全排列
# Problem Url:  https://leetcode-cn.com/problems/VvJkup/
# Problem Level:  Medium
 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            res = []
            for i in range(len(nums)):
                t = self.permute(nums[:i]+nums[(i+1):])
                res += [[nums[i]]+u for u in t]
            return res