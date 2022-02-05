# Problem Id:  844
# Problem Name:  Backspace String Compare, 比较含退格的字符串
# Problem Url:  https://leetcode-cn.com/problems/backspace-string-compare/
# Problem Level:  Easy
 
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = []
        t = []
        for i in range(len(S)):
            if S[i] == '#':
                if len(s) != 0:
                    del s[-1]
            else:
                s.append(S[i])
        for i in range(len(T)):
            if T[i] == '#':
                if len(t) != 0:
                    del t[-1]
            else:
                t.append(T[i])
        return s == t
                    