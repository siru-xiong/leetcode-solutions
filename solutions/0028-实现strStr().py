# Problem Id:  28
# Problem Name:  Implement strStr(), 实现 strStr()
# Problem Url:  https://leetcode-cn.com/problems/implement-strstr/
# Problem Level:  Easy
 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        elif len(needle) > len(haystack):
            return -1
        else:
            result = -1
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i:(i+len(needle))] == needle:
                    result = i
                    break
            return result