# Problem Id:  1071
# Problem Name:  Greatest Common Divisor of Strings, 字符串的最大公因子
# Problem Url:  https://leetcode-cn.com/problems/greatest-common-divisor-of-strings/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) < len(str1):
            str1 , str2 = str2 , str1
        res = ''

        for i in range(1,len(str1)+1):
            if (len(str1) % i == 0) and (len(str2) % i == 0):
                t = str1[:i]
                if t * (len(str1) // i) == str1 and t * (len(str2) // i) == str2:
                    res = t
        return res

