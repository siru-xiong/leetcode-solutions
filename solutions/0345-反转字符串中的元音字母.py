# Problem Id:  345
# Problem Name:  Reverse Vowels of a String, 反转字符串中的元音字母
# Problem Url:  https://leetcode-cn.com/problems/reverse-vowels-of-a-string/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        if len(s) >= 2:
            i = 0
            j = len(s)-1
            while True:
                if s[i] not in vowel:
                    i = i + 1
                if s[j] not in vowel:
                    j = j - 1
                if s[i] in vowel and s[j] in vowel:
                    s[i],s[j] = s[j],s[i]
                    i,j = i+1,j-1
                if i - j >= 0:
                    break
        return ''.join(s)