# Problem Id:  191
# Problem Name:  Number of 1 Bits, 位1的个数
# Problem Url:  https://leetcode-cn.com/problems/number-of-1-bits/
# Problem Level:  Easy
 
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')