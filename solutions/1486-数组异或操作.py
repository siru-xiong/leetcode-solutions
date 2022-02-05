# Problem Id:  1486
# Problem Name:  XOR Operation in an Array, 数组异或操作
# Problem Url:  https://leetcode-cn.com/problems/xor-operation-in-an-array/
# Problem Level:  Easy
 
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans ^= start + 2*i
        return ans