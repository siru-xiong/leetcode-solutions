# Problem Id:  7
# Problem Name:  Reverse Integer, 整数反转
# Problem Url:  https://leetcode-cn.com/problems/reverse-integer/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            neg = 1
        else:
            neg = 0
        x = str(abs(x))
        leng = len(x)
        temp = leng - 1
        result = 0
        for i in range(1,leng+1):
            result = result + int(x[-i]) * pow(10,temp)
            temp = temp - 1
        
        if neg == 1:
            if result > 2147483648:
                result = 0
            else:
                result = - result
        else:
            if result > 2147483647:
                result = 0       

        return result

