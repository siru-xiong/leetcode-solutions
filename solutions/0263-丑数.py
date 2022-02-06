# Problem Id:  263
# Problem Name:  Ugly Number, 丑数
# Problem Url:  https://leetcode-cn.com/problems/ugly-number/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        else:
            while num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
                if num % 2 == 0:
                    num = num // 2
                if num % 3 == 0:
                    num = num // 3
                if num % 5 == 0:
                    num = num // 5
            return num == 1
            