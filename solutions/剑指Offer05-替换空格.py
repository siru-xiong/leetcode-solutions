# Problem Id:  剑指 Offer 05
# Problem Name:  替换空格 LCOF, 替换空格
# Problem Url:  https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for i in s:
            if i == ' ':
                res += '%20'
            else:
                res += i
        return res