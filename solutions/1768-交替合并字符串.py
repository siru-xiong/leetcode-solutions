# Problem Id:  1768
# Problem Name:  Merge Strings Alternately, 交替合并字符串
# Problem Url:  https://leetcode-cn.com/problems/merge-strings-alternately/
# Problem Level:  Easy
 
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        res = ''
        while i < len(word1) and j < len(word2):
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1
        if i < len(word1):
            res += word1[i:]
        if j < len(word2):
            res += word2[j:]
        return res