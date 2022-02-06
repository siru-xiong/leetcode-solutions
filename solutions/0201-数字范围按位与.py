# Problem Id:  201
# Problem Name:  Bitwise AND of Numbers Range, 数字范围按位与
# Problem Url:  https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:
            left >>= 1
            right >>= 1
            i += 1
        return right << i