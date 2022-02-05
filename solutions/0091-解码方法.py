# Problem Id:  91
# Problem Name:  Decode Ways, 解码方法
# Problem Url:  https://leetcode-cn.com/problems/decode-ways/
# Problem Level:  Medium
 
class Solution:
    def __init__(self):
        self.dict = {}

    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            if s[0] =='0':
                return 0
            else:
                return 1
        elif len(s) == 2:
            if s[0] == '0':
                return 0
            elif int(s) <= 26 and s[1] != '0':
                return 2
            elif int(s) <= 26 and s[1] == '0':
                return 1
            elif s[1] == '0':
                return 0
            else:
                return 1
        else:
            if s in self.dict:
                return self.dict[s]
            if s[0] == '0':
                self.dict[s] = 0
                return 0
            else:
                if s[1:] in self.dict:
                    res = self.dict[s[1:]]
                else:
                    res = self.numDecodings(s[1:])
                    self.dict[s[1:]] = res

                if int(s[:2]) <= 26:
                    if s[2:] in self.dict:
                        self.dict[s] = res + self.dict[s[2:]]
                        return res + self.dict[s[2:]]
                    else:
                        t = self.numDecodings(s[2:])
                        self.dict[s[2:]] = t
                        self.dict[s] = res + t
                        return res + t
                else:
                    self.dict[s] = res
                    return res
