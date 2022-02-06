# Problem Id:  409
# Problem Name:  Longest Palindrome, 最长回文串
# Problem Url:  https://leetcode-cn.com/problems/longest-palindrome/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0) + 1
        result = 0
        temp = 0
        for i in range(len(s)):
            if count[s[i]] % 2 == 0:
                result = result + count[s[i]]
                count[s[i]] = -1
            elif count[s[i]] != -1:
                temp = 1
                result = result + count[s[i]] - 1
                count[s[i]] = -1
        if temp == 1:
            return result+1
        else:
            return result


