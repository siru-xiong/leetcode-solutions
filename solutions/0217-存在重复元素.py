# Problem Id:  217
# Problem Name:  Contains Duplicate, 存在重复元素
# Problem Url:  https://leetcode-cn.com/problems/contains-duplicate/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)