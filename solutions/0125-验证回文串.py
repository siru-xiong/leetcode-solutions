# Problem Id:  125
# Problem Name:  Valid Palindrome, 验证回文串
# Problem Url:  https://leetcode-cn.com/problems/valid-palindrome/
# Problem Level:  Easy
 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = []
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                result.append(s[i])
        s = ''.join(result)
        length = len(s)
        if len(s) == 0:
            return True
        i = 0
        j = len(s)-1
        result = True
        while True:
            if s[i] == s[j]:
                i = i + 1
                j = j - 1
            else:
                result = False
                break
            if i-j >= 0:
                break
        return result