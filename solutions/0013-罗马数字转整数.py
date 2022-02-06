# Problem Id:  13
# Problem Name:  Roman to Integer, 罗马数字转整数
# Problem Url:  https://leetcode-cn.com/problems/roman-to-integer/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        index = 0
        s = s + ' '
        while True:
            if s[index] == 'I':
                if s[index+1] == 'V':
                    result = result + 4
                    index = index +2
                elif s[index+1] == 'X':
                    result = result + 9
                    index = index + 2
                else:
                    result = result + 1
                    index = index + 1
            elif s[index] == 'V':
                result = result + 5
                index = index + 1
            elif s[index] == 'X':
                if s[index +1] == 'L':
                    result = result + 40
                    index = index + 2
                elif s[index + 1] == 'C':
                    result = result + 90
                    index = index + 2
                else:
                    result = result + 10
                    index = index + 1
            elif s[index] == 'L':
                result = result + 50
                index = index + 1
            elif s[index] == 'C':
                if s[index+ 1] == 'D':
                    result = result + 400
                    index = index +2
                elif s[index + 1] == 'M':
                    result = result + 900
                    index = index +2
                else:
                    result = result + 100
                    index = index +1
            elif s[index] == 'D':
                result = result + 500
                index = index +1
            elif s[index] == 'M':
                result = result + 1000
                index = index + 1

            elif s[index] == ' ':
                break
        return result                 