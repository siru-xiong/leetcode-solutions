# Problem Id:  137
# Problem Name:  Single Number II, 只出现一次的数字 II
# Problem Url:  https://leetcode-cn.com/problems/single-number-ii/
# Problem Level:  Medium
 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0 
        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)
        return seen_once