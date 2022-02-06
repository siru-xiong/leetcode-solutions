# Problem Id:  628
# Problem Name:  Maximum Product of Three Numbers, 三个数的最大乘积
# Problem Url:  https://leetcode-cn.com/problems/maximum-product-of-three-numbers/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min_result = [nums[0],float('inf')]
        max_result = [nums[0],float('-inf'),float('-inf')]
        for i in range(1,len(nums)):
            if nums[i] >= max_result[0]:
                del max_result[2]
                max_result = [nums[i]] + max_result
            elif nums[i] >= max_result[1]:
                max_result = [max_result[0] ,nums[i], max_result[1]]
            elif nums[i] >= max_result[2]:
                del max_result[2]
                max_result.append(nums[i])

            if nums[i] <= min_result[0]:
                del min_result[1]
                min_result = [nums[i]] + min_result
            elif nums[i] <= min_result[1]:
                min_result = [min_result[0],nums[i]]
        if max_result[0] <= 0:
            return max_result[0]*max_result[1]*max_result[2]
        else:
            return max(max_result[0]*max_result[1]*max_result[2],min_result[0]*min_result[1]*max_result[0])