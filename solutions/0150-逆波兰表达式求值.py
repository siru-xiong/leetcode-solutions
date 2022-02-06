# Problem Id:  150
# Problem Name:  Evaluate Reverse Polish Notation, 逆波兰表达式求值
# Problem Url:  https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '*':
                t = stack[-2]*stack[-1]
                del stack[-1]
                del stack[-1]
                stack.append(t)
            elif i == '/':
                if stack[-2] < 0 and stack[-1] > 0 or stack[-2] > 0 and stack[-1] < 0:
                    t = - (abs(stack[-2]) // abs(stack[-1]))
                else:
                    t = stack[-2] // stack[-1]
                del stack[-1]
                del stack[-1]
                stack.append(t)
            elif i == '+':
                t = stack[-2]+stack[-1]
                del stack[-1]
                del stack[-1]
                stack.append(t)
            elif i == '-':
                t = stack[-2]-stack[-1]
                del stack[-1]
                del stack[-1]
                stack.append(t)
            else:
                stack.append(int(i))
        return stack[-1]