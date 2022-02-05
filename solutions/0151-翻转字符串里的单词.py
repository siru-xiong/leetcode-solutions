# Problem Id:  151
# Problem Name:  Reverse Words in a String, 翻转字符串里的单词
# Problem Url:  https://leetcode-cn.com/problems/reverse-words-in-a-string/
# Problem Level:  Medium
 
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([i for i in s.split()][::-1])