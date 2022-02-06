# Problem Id:  5
# Problem Name:  Longest Palindromic Substring, 最长回文子串
# Problem Url:  https://leetcode-cn.com/problems/longest-palindromic-substring/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        for i in range(len(s)):
            c = 1
            j = 1
            while i-j>=0 and i+j<=len(s)-1:
                if s[i-j] == s[i+j]:
                    c = c + 2
                    j = j + 1
                else:
                    break
            if c > res:
                res = c
                output = s[(i-j+1):(i+j)]
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                c = 2
                j = 1
                while i-1-j>=0 and i+j<=len(s)-1:
                    if s[i-1-j] == s[i+j]:
                        c = c+ 2
                        j = j + 1
                    else:
                        break
                if c >res:
                    res = c
                    output = s[(i-j):(i+j)]
        return output