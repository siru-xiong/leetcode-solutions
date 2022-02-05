# Problem Id:  1748
# Problem Name:  Sum of Unique Elements, 唯一元素的和
# Problem Url:  https://leetcode-cn.com/problems/sum-of-unique-elements/
# Problem Level:  Easy
 
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ct = {}
        for i in range(len(nums)):
            ct[nums[i]] = ct.get(nums[i],0)+1
        res = 0
        for j in ct:
            if ct[j] == 1:
                res += j
        return res