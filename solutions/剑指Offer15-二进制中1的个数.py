# Problem Id:  剑指 Offer 15
# Problem Name:  二进制中1的个数 LCOF, 二进制中1的个数
# Problem Url:  https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/
# Problem Level:  Easy
 
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res