# Problem Id:  561
# Problem Name:  Array Partition I, 数组拆分 I
# Problem Url:  https://leetcode-cn.com/problems/array-partition-i/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])