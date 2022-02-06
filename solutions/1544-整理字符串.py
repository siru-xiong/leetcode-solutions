# Problem Id:  1544
# Problem Name:  Make The String Great, 整理字符串
# Problem Url:  https://leetcode-cn.com/problems/make-the-string-great/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            else:
                if i.islower() and i.upper() == stack[-1] or i.isupper() and i.lower() == stack[-1]:
                    del stack[-1]
                else:
                    stack.append(i)
        return ''.join(stack)
