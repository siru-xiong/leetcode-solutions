# Problem Id:  剑指 Offer 67
# Problem Name:  把字符串转换成整数 LCOF, 把字符串转换成整数
# Problem Url:  https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/
# Problem Level:  Medium
 
class Solution:
    def strToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0
        s = list(s)
        while True:
            if s[0] == ' ':
                del s[0]
            else:
                break
            if len(s) == 0:
                break
        n = 0
        if len(s) == 0:
            return 0
        if s[0] in ('+','-'):
            if s[0] == '-':
                n = 1
            s = s[1:]
        index = -1
        for i in range(len(s)):
            if s[i].isdigit():
                index = i
            else:
                break
        if index == -1:
            return 0
        else:
            s = s[:(index+1)]
        res = 0
        i = 0
        while True:
            if i <= len(s)-1:
                res = res * 10
                res = res + int(s[i])
                i = i + 1
            else:
                break
        if n == 1:
            res = - res
        if res >= 0 and res > 2147483647:
            return 2147483647
        elif res >= 0:
            return res
        if res < 0 and res < -2147483648:
            return -2147483648
        else:
            return res
    