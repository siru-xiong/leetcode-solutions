# Problem Id:  2063
# Problem Name:  Vowels of All Substrings, 所有子字符串中的元音
# Problem Url:  https://leetcode-cn.com/problems/vowels-of-all-substrings/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def countVowels(self, word: str) -> int:
        res = 0
        n = len(word)
        for i in range(n):
            if word[i] in ["a","e","i","o","u"]:
                res += (i+1)*(n-i)
        return res