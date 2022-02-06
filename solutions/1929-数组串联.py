# Problem Id:  1929
# Problem Name:  Concatenation of Array, 数组串联
# Problem Url:  https://leetcode-cn.com/problems/concatenation-of-array/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums