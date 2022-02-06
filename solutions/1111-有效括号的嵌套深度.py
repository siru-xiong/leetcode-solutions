# Problem Id:  1111
# Problem Name:  Maximum Nesting Depth of Two Valid Parentheses Strings, 有效括号的嵌套深度
# Problem Url:  https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        d = 0
        for c in seq:
            if c == '(':
                d += 1
                ans.append(d % 2)
            if c == ')':
                ans.append(d % 2)
                d -= 1
        return ans