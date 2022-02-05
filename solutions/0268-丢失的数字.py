# Problem Id:  268
# Problem Name:  Missing Number, 丢失的数字
# Problem Url:  https://leetcode-cn.com/problems/missing-number/
# Problem Level:  Easy
 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        vset = set(nums)
        for i in range(len(nums)+1):
            if i not in vset:
                return i