# Problem Id:  921
# Problem Name:  Minimum Add to Make Parentheses Valid, 使括号有效的最少添加
# Problem Url:  https://leetcode-cn.com/problems/minimum-add-to-make-parentheses-valid/
# Problem Level:  Medium
 
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for i in S:
            if i == '(':
                stack.append(i)
            else:
                if len(stack) >= 1 and stack[-1] == '(':
                    del stack[-1]
                else:
                    stack.append(i)
        return len(stack)