# Problem Id:  1
# Problem Name:  Two Sum, 两数之和
# Problem Url:  https://leetcode-cn.com/problems/two-sum/
# Problem Level:  Easy
 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                    break