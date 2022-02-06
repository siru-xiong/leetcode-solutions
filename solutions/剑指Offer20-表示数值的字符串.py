# Problem Id:  剑指 Offer 20
# Problem Name:  表示数值的字符串 LCOF, 表示数值的字符串
# Problem Url:  https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def block(self, s:str) -> bool:
        res = list(s)
        while True:
            if res[0] == ' ':
                del res[0]
            else:
                break
            if len(res) == 0:
                break
        if len(res) == 0:
            return ''
        else:
            while True:
                if res[-1] == ' ':
                    del res[-1]
                else:
                    break
            return ''.join(res)

    def pt(self, s: str) -> bool:
        p = []
        for i in range(len(s)):
            if s[i] == '.':
                p.append(i)
            elif not s[i].isdigit():
                return False
        if len(p) >= 2:
            return False
        elif len(p) == 1:
            if p[0] == len(s)-1:
                return self.inte(s[:(-1)])
            elif p[0] == 0:
                return self.inte(s[1:])
            else:
                return self.inte(s[:p[0]]) and self.inte(s[(p[0]+1):])
        elif len(p) == 0:
            return self.inte(s)

    def inte(self, s: str) -> bool:
        if len(s) == 0:
            return False
        for i in s:
            if not i.isdigit():
                return False
        return True

    def isNumber(self, s: str) -> bool:
        if len(s) == 0:
            return False
        s = self.block(s)
        if len(s) == 0:
            return False
        e = []
        for i in range(len(s)):
            if s[i] in ('e','E'):
                e.append(i)
        if len(e) >= 2:
            return False
        elif len(e) == 0:
            if s[0] in ('+','-'):
                s = s[1:]
                return self.pt(s)
            else:
                return self.pt(s)
        elif len(e) == 1:
            if e[0] == 0 or e[0] >= len(s) - 1:
                return False
            else:
                if s[e[0]+1] in ('+','-'):
                    if s[0] in ('+','-'):
                        return self.pt(s[1:e[0]]) and self.inte(s[(e[0]+2):])
                    else:
                        return self.pt(s[:e[0]]) and self.inte(s[(e[0]+2):])
                else:
                    if s[0] in ('+','-'):
                         return self.pt(s[1:e[0]]) and self.inte(s[(e[0]+1):])
                    else:
                        return self.pt(s[:e[0]]) and self.inte(s[(e[0]+1):])