# Problem Id:  357
# Problem Name:  Count Numbers with Unique Digits, 计算各个位数不同的数字个数
# Problem Url:  https://leetcode-cn.com/problems/count-numbers-with-unique-digits/
# Problem Level:  Medium
 
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 10
        elif n == 2:
            return 91
        else:
            return self.C(n)*self.A(n) + self.C(n-1)*(n-1)*self.A(n-1) + self.countNumbersWithUniqueDigits(n-1)

    def A(self,n):
        t = [1,1,2,6,24,120,720,5040,40320,362880,3628800]
        return t[n]
    
    def C(self,n):
        if n >= 10:
            return 0
        else:
            t = 9
            res = 1
            for i in range(n):
                res *= t
                t -= 1
            t = [1,1,2,6,24,120,720,5040,40320,362880,3628800]
            res //= t[n]
            return res