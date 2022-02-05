# Problem Id:  152
# Problem Name:  Maximum Product Subarray, 乘积最大子数组
# Problem Url:  https://leetcode-cn.com/problems/maximum-product-subarray/
# Problem Level:  Medium
 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minres = [nums[0]]
        maxres = [nums[0]]
        for i in range(1,len(nums)):
            c = min(minres[-1]*nums[i],maxres[-1]*nums[i],nums[i])
            t = max(minres[-1]*nums[i],maxres[-1]*nums[i],nums[i])
            minres.append(c)
            maxres.append(t)
        return max(maxres)
