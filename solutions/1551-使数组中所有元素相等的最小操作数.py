# Problem Id:  1551
# Problem Name:  Minimum Operations to Make Array Equal, 使数组中所有元素相等的最小操作数
# Problem Url:  https://leetcode-cn.com/problems/minimum-operations-to-make-array-equal/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def minOperations(self, n: int) -> int:
        t = 0
        for i in range(1,2*n+1,2):
            t = t + abs(i-n)
        return t // 2