# Problem Id:  面试题 01.03
# Problem Name:  String to URL LCCI, URL化
# Problem Url:  https://leetcode-cn.com/problems/string-to-url-lcci/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(' ','%20')