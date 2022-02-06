# Problem Id:  58
# Problem Name:  Length of Last Word, 最后一个单词的长度
# Problem Url:  https://leetcode-cn.com/problems/length-of-last-word/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')
        r = 0
        for i in range(len(s)-1,-1,-1):
            if len(s[i]) != 0:
                r = len(s[i])
                break
        return r