# Problem Id:  1021
# Problem Name:  Remove Outermost Parentheses, 删除最外层的括号
# Problem Url:  https://leetcode-cn.com/problems/remove-outermost-parentheses/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        S = list(S)
        start = 0
        i = 0
        c = 0
        while True:
            if S[i] == '(':
                c = c + 1
            else:
                c = c - 1
            if c == 0:
                del S[start]
                del S[i-1]
                start = i - 1
                i = i - 1
            else:
                i = i + 1
            if i >= len(S):
                break
        return ''.join(S)