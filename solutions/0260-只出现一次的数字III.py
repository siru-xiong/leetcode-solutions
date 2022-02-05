# Problem Id:  260
# Problem Name:  Single Number III, 只出现一次的数字 III
# Problem Url:  https://leetcode-cn.com/problems/single-number-iii/
# Problem Level:  Medium
 
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]