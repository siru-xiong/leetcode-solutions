# Problem Id:  414
# Problem Name:  Third Maximum Number, 第三大的数
# Problem Url:  https://leetcode-cn.com/problems/third-maximum-number/
# Problem Level:  Easy
 
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            result = [nums[0],float('-inf'),float('-inf')]
            for i in range(len(nums)):
                if nums[i] > result[0]:
                    del result[2]
                    result = [nums[i]] + result
                elif nums[i] != result[0] and nums[i] > result[1]:
                    result = [result[0] ,nums[i], result[1]]
                elif nums[i] != result[0] and nums[i] != result[1] and nums[i] > result[2]:
                    del result[2]
                    result.append(nums[i])
            if result[2] != float('-inf'):
                return result[2]
            else:
                return result[0]
