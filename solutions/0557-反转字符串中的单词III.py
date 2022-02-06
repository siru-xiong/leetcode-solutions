# Problem Id:  557
# Problem Name:  Reverse Words in a String III, 反转字符串中的单词 III
# Problem Url:  https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([i[::-1] for i in s.split(' ')])