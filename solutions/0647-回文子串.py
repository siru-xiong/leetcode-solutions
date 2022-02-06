# Problem Id:  647
# Problem Name:  Palindromic Substrings, 回文子串
# Problem Url:  https://leetcode-cn.com/problems/palindromic-substrings/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res = res + 1
            j = 1
            while i-j>=0 and i+j<len(s) and s[i-j] == s[i+j]:
                res = res + 1
                j = j + 1

        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                res = res + 1
                j = 1
                while i-1-j>=0 and i+j<len(s) and s[i-j-1] == s[i+j]:
                    res = res + 1
                    j = j + 1
        return res