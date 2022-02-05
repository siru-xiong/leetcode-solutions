# Problem Id:  1221
# Problem Name:  Split a String in Balanced Strings, 分割平衡字符串
# Problem Url:  https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/
# Problem Level:  Easy
 
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        l = 0
        count = 0
        for i in range(len(s)):
            if s[i] == 'R':
                r = r + 1
            else:
                l = l + 1
            if r == l:
                count = count + 1
                r = 0
                l = 0
        return count