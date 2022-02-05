# Problem Id:  537
# Problem Name:  Complex Number Multiplication, 复数乘法
# Problem Url:  https://leetcode-cn.com/problems/complex-number-multiplication/
# Problem Level:  Medium
 
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        i1 = 0
        i2 = 0
        for i in range(len(a)):
            if a[i] == '+':
                i1 = i
                break
        for i in range(len(b)):
            if b[i] == '+':
                i2 = i
                break
        p = int(a[:i1])
        q = int(a[(i1+1):(-1)])
        r = int(b[:i2])
        s = int(b[(i2+1):(-1)])
        
        x = p*r - q*s
        y = p*s + q*r

        return str(x)+'+'+str(y)+'i'