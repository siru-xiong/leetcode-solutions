# Problem Id:  394
# Problem Name:  Decode String, 字符串解码
# Problem Url:  https://leetcode-cn.com/problems/decode-string/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def decodeString(self, s: str) -> str:
        res  = ''
        i = 0
        while i < len(s):
            if s[i].isalpha():
                res = res + s[i]
                i = i + 1
            elif s[i].isdigit():
                y = i
                while i+1<len(s) and s[i+1].isdigit():
                    i = i + 1
                repeat = int(s[y:(i+1)])
                print(repeat)
                start = i + 2
                i = start
                t = 1
                while True:
                    if s[i] == '[':
                        t = t + 1
                    elif s[i] == ']':
                        t = t - 1
                    i = i + 1
                    if t == 0:
                        break
                end = i
                temp = self.decodeString(s[start:(end-1)])
                res = res + temp * repeat
        return res
