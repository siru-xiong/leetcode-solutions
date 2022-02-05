# Problem Id:  1056
# Problem Name:  Confusing Number, 易混淆数
# Problem Url:  https://leetcode-cn.com/problems/confusing-number/
# Problem Level:  Easy
 
class Solution:
    def confusingNumber(self, n: int) -> bool:
        k = n
        def m(x):
            t = [0,1,-1,-1,-1,-1,9,-1,8,6]
            return t[x]
        n = [m(int(i)) for i in list(str(n))][::-1]
        for i in n:
            if i == -1:
                return False
        return int(''.join([str(i) for i in n])) != k

