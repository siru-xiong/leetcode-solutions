# Problem Id:  面试题 05.06
# Problem Name:  Convert Integer LCCI, 整数转换
# Problem Url:  https://leetcode-cn.com/problems/convert-integer-lcci/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        return bin((A ^ B) & 0xffffffff).count('1')