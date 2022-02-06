# Problem Id:  453
# Problem Name:  Minimum Moves to Equal Array Elements, 最小操作次数使数组元素相等
# Problem Url:  https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        a = min(nums)
        return sum([i-a for i in nums])