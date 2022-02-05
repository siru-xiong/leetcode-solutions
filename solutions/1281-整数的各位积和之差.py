# Problem Id:  1281
# Problem Name:  Subtract the Product and Sum of Digits of an Integer, 整数的各位积和之差
# Problem Url:  https://leetcode-cn.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# Problem Level:  Easy
 
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(str(n))
        n = [int(i) for i in n]
        m = 1
        for i in n:
            m = m*i
        return m -sum(n)