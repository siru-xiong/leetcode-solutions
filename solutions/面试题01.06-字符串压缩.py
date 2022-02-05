# Problem Id:  面试题 01.06
# Problem Name:  Compress String LCCI, 字符串压缩
# Problem Url:  https://leetcode-cn.com/problems/compress-string-lcci/
# Problem Level:  Easy
 
class Solution:
    def compressString(self, S: str) -> str:
        if len(S) == 0:
            return ''
        res = S[0]
        start = S[0]
        i = 1
        t = S
        S = S[1:]
        for s in S:
            if s == start:
                i += 1
            else:
                res += str(i)
                i = 1
                start = s
                res += s
        res += str(i)
        if len(res) < len(t):
            return res
        else:
            return t

