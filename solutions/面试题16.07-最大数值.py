# Problem Id:  面试题 16.07
# Problem Name:  Maximum LCCI, 最大数值
# Problem Url:  https://leetcode-cn.com/problems/maximum-lcci/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def maximum(self, a: int, b: int) -> int:
        return ((a + b) + abs(a - b)) // 2