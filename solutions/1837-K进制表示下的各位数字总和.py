# Problem Id:  1837
# Problem Name:  Sum of Digits in Base K, K 进制表示下的各位数字总和
# Problem Url:  https://leetcode-cn.com/problems/sum-of-digits-in-base-k/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        while n != 0:
            res += n % k
            n //= k
        return res