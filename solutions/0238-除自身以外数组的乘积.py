# Problem Id:  238
# Problem Name:  Product of Array Except Self, 除自身以外数组的乘积
# Problem Url:  https://leetcode-cn.com/problems/product-of-array-except-self/
# Problem Level:  Medium
 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        temp = 1
        for i in range(len(nums)):
            res[i] = res[i] * temp
            temp = temp * nums[i]
        temp = 1
        for i in range(1,len(nums)+1):
            res[-i] = res[-i] * temp
            temp = temp * nums[-i]
        return res
