# Problem Id:  392
# Problem Name:  Is Subsequence, 判断子序列
# Problem Url:  https://leetcode-cn.com/problems/is-subsequence/
# Problem Level:  Easy
 
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i = i + 1
                j = j + 1
            else:
                j = j + 1
        return i == len(s)