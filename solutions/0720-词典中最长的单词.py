# Problem Id:  720
# Problem Name:  Longest Word in Dictionary, 词典中最长的单词
# Problem Url:  https://leetcode-cn.com/problems/longest-word-in-dictionary/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        record, res = set(), ""
        for word in words:
            if word[:-1] in record or word[:-1] == "":
                if len(word) > len(res):
                    res = word
                record.add(word)
        return res