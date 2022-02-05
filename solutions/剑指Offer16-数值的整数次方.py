# Problem Id:  剑指 Offer 16
# Problem Name:  数值的整数次方 LCOF, 数值的整数次方
# Problem Url:  https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/
# Problem Level:  Medium
 
class Solution:
    def Pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == 2:
            return x*x
        else:
            t = self.Pow(x,n // 2)
            if n % 2 == 0:
                return t*t
            else:
                return t*t*x
    
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.Pow(x,n)
        else:
            return 1/self.Pow(x,-n)