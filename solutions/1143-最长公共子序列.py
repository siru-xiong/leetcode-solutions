# Problem Id:  1143
# Problem Name:  Longest Common Subsequence, 最长公共子序列
# Problem Url:  https://leetcode-cn.com/problems/longest-common-subsequence/
# Problem Level:  Medium
 
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        res = [ [0 for _ in range(n)] for _ in range(m)]
        x = 0
        for i in range(n):
            if x == 1:
                res[0][i] = 1
            elif text1[0] == text2[i]:
                x = 1
                res[0][i] = 1
        y = 0
        for j in range(m):
            if y == 1:
                res[j][0] = 1
            elif text2[0] == text1[j]:
                y = 1
                res[j][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                if text1[i] == text2[j]:
                    res[i][j] = res[i-1][j-1] + 1
                else:
                    res[i][j] = max(res[i-1][j],res[i][j-1])
        return res[-1][-1]