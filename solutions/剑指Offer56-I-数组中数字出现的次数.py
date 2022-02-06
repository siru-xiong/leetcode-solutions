# Problem Id:  剑指 Offer 56 - I
# Problem Name:  数组中数字出现的次数 LCOF, 数组中数字出现的次数
# Problem Url:  https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        r = 0
        for i in nums:
            r ^= i
        d = 1
        while d & r == 0:
            d <<= 1
        a,b = 0,0
        for i in nums:
            if i & d:
                a ^= i
            else:
                b ^= i
        return [a,b]