# Problem Id:  227
# Problem Name:  Basic Calculator II, 基本计算器 II
# Problem Url:  https://leetcode-cn.com/problems/basic-calculator-ii/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def calculate(self, s: str) -> int:
        s = s + '*1'
        stack = []
        t = ''
        m = 0
        n = 0
        u = 0
        for i in range(len(s)):
            if s[i] == ' ':
                pass
            elif s[i] in ('+','-','*','/'):
                t = int(t)
                if m == 1:
                    stack[-1] = stack[-1] * t
                    m = 0
                elif n == 1:
                    if stack[-1] > 0:
                        stack[-1] = stack[-1] // t
                    else:
                        stack[-1] = -((-stack[-1]) // t)
                    n = 0
                else:
                    if u == 1:
                        t = -t
                        u = 0
                    stack.append(t)
                
                if s[i] == '*':
                    m = 1
                if s[i] == '/':
                    n = 1
                if s[i] == '-':
                    u = 1
                t = ''
            else:
                t = t + s[i]
        return sum(stack)
                


            