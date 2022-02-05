# Problem Id:  剑指 Offer 50
# Problem Name:  第一个只出现一次的字符  LCOF, 第一个只出现一次的字符
# Problem Url:  https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
# Problem Level:  Easy
 
class Solution:
    def firstUniqChar(self, s: str) -> str:
        e = {}
        for i in s:
            e[i] = e.get(i,0) + 1
        for i in s:
            if e[i] == 1:
                return i
        return " "