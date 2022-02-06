# Problem Id:  169
# Problem Name:  Majority Element, 多数元素
# Problem Url:  https://leetcode-cn.com/problems/majority-element/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            result = nums[0]
            count = 1
            for i in range(1,len(nums)):
            
                if nums[i] == result:
                    count = count + 1
                else:
                    count = count - 1
                if count < 0:
                    result = nums[i]
                    count = 1
            return result
