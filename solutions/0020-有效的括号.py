# Problem Id:  20
# Problem Name:  Valid Parentheses, 有效的括号
# Problem Url:  https://leetcode-cn.com/problems/valid-parentheses/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        else:    
            l = [s[0]]
            for i in range(1,len(s)):
                if len(l) != 0 and ((l[-1] == '(' and s[i] == ')') or (l[-1] == '{' and s[i] == '}') or (l[-1] == '[' and s[i] == ']')):
                        l.pop(-1)
                else:
                    l = l + [s[i]]
            if len(l) == 0:
                return True
            else:
                return False

