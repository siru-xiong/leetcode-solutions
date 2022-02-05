# Problem Id:  1464
# Problem Name:  Maximum Product of Two Elements in an Array, 数组中两元素的最大乘积
# Problem Url:  https://leetcode-cn.com/problems/maximum-product-of-two-elements-in-an-array/
# Problem Level:  Easy
 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        v = [float('-inf'),float('-inf')]
        for i in nums:
            if i > v[0]:
                v = [i,v[0]]
            elif i > v[1]:
                v = [v[0],i]
        return (v[0]-1) * (v[1]-1)