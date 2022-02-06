# Problem Id:  43
# Problem Name:  Multiply Strings, 字符串相乘
# Problem Url:  https://leetcode-cn.com/problems/multiply-strings/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'
        str1 = {}
        str2 = {}
        for i in range(len(num1)):
            str1[i] = int(num1[-(i+1)])
        for i in range(len(num2)):
            str2[i] = int(num2[-(i+1)])
        re = 0
        k = 10**(len(num1)+len(num2)-2)
        for i in range(len(num1)+len(num2)-2,-1,-1):
            for m in range(min(i+1,len(num1))):
                if i-m < len(num2):
                    re = re + str1[m]*str2[i-m]*k
            k = k // 10
        return str(re)