# Problem Id:  1920
# Problem Name:  Build Array from Permutation, 基于排列构建数组
# Problem Url:  https://leetcode-cn.com/problems/build-array-from-permutation/
# Problem Level:  Easy
 
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]