# Problem Id:  面试题19
# Problem Name:  正则表达式匹配 LCOF, 正则表达式匹配
# Problem Url:  https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/
# Problem Level:  Hard
# Language:  Python3
 
class Solution:
    def b(self,p):
        p = list(p)
        for i in range(len(p)):
            if p[i] == '*':
                p[i-1] = '*'+p[i-1]
        i = 0
        while i < len(p):
            if p[i] == '*':
                del p[i]
            i += 1
        return p

    def match(self,s,p):
        if len(p) == 0:
            if len(s) == 0:
                return True
            else:
                return False
        elif len(p) == 1:
            if len(p[0]) == 2:
                if len(s) == 0:
                    return True
                if p[0][1] == '.':
                    return True
                else:
                    return set(s) == set([p[0][1]])
            elif p[0] == '.':
                return len(s) == 1
            else:
                return len(s) == 1 and s[0] == p[0][0]
        else:
            if len(p[0]) == 2:
                res = False
                res = res or self.match(s,p[1:])
                if res:
                    return True
                if p[0][1] == '.':
                    for i in range(len(s)):
                        res = res or self.match(s[(i+1):],p[1:])
                        if res:
                            return res
                    return res
                else:
                    for i in range(len(s)):
                        if s[i] == p[0][1]:
                            res = res or self.match(s[(i+1):],p[1:])
                            if res:
                                return res
                        else:
                            break
                    return res
            elif p[0] == '.':
                if len(s) == 0:
                    return False
                else:
                    return self.match(s[1:],p[1:])    
            else:
                if len(s) == 0:
                    return False
                elif s[0] != p[0]:
                    return False
                else:
                    return self.match(s[1:],p[1:])

    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            if len(s) == 0:
                return True
            else:
                return False
        else:
            p = self.b(p)
            return self.match(s,p)