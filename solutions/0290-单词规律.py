# Problem Id:  290
# Problem Name:  Word Pattern, 单词规律
# Problem Url:  https://leetcode-cn.com/problems/word-pattern/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p2s = dict()
        s2p = dict()
        s = s.split()
        if len(pattern) != len(s):
            return False
        else:
            result = True
            for i in range(len(s)):
                if (pattern[i] in p2s and p2s[pattern[i]] != s[i]) or (s[i] in s2p and s2p[s[i]] != pattern[i]):
                    result = False
                    break
                p2s[pattern[i]] = s[i]
                s2p[s[i]] = pattern[i]
            return result
