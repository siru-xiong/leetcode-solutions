# Problem Id:  50
# Problem Name:  Pow(x, n), Pow(x, n)
# Problem Url:  https://leetcode-cn.com/problems/powx-n/
# Problem Level:  Medium
# Language:  Python3
 
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
