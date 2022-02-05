# Problem Id:  1863
# Problem Name:  Sum of All Subset XOR Totals, 找出所有子集的异或总和再求和
# Problem Url:  https://leetcode-cn.com/problems/sum-of-all-subset-xor-totals/
# Problem Level:  Easy
 
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x|y, nums) << (len(nums)-1)