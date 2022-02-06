# Problem Id:  1309
# Problem Name:  Decrypt String from Alphabet to Integer Mapping, 解码字母到整数映射
# Problem Url:  https://leetcode-cn.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ''
        i = len(s)-1
        while True:
            if s[i] == '#':
                res = chr(int(s[(i-2):i]) + 96) + res
                i = i - 3
            else:
                res = chr(int(s[i])+96) + res
                i = i - 1
            if i <= -1:
                break
        return res