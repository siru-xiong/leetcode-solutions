# Problem Id:  1614
# Problem Name:  Maximum Nesting Depth of the Parentheses, 括号的最大嵌套深度
# Problem Url:  https://leetcode-cn.com/problems/maximum-nesting-depth-of-the-parentheses/
# Problem Level:  Easy
 
class Solution:
    def maxDepth(self, s: str) -> int:
        d = 0
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
                if len(stack) > d:
                    d = len(stack)
            elif i == ')':
                if stack[-1] == '(':
                    del stack[-1]
        return d