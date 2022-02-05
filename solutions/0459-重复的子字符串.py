# Problem Id:  459
# Problem Name:  Repeated Substring Pattern, 重复的子字符串
# Problem Url:  https://leetcode-cn.com/problems/repeated-substring-pattern/
# Problem Level:  Easy
 
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]