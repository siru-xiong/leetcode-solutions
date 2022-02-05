# Problem Id:  172
# Problem Name:  Factorial Trailing Zeroes, 阶乘后的零
# Problem Url:  https://leetcode-cn.com/problems/factorial-trailing-zeroes/
# Problem Level:  Medium
 
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0
        current_multiple = 5
        while n >= current_multiple:
            zero_count += n // current_multiple
            current_multiple *= 5
        return zero_count