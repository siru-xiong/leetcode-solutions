# Problem Id:  剑指 Offer II 095
# Problem Name:  最长公共子序列, 最长公共子序列
# Problem Url:  https://leetcode-cn.com/problems/qJnOS7/
# Problem Level:  Medium
 
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = []
        for i in range(len(text1)):
            res.append([0]*len(text2))
        t = 0
        for i in range(len(text2)):
            if text1[0] == text2[i]:
                t = 1
            if t == 1:
                res[0][i] = 1
        t = 0
        for j in range(len(text1)):
            if text1[j] == text2[0]:
                t = 1
            if t == 1:
                res[j][0] = 1
        for i in range(1,len(text1)):
            for j in range(1,len(text2)):
                if text1[i] == text2[j]:
                    res[i][j] = res[i-1][j-1] + 1
                else:
                    res[i][j] = max(res[i-1][j],res[i][j-1])
        return res[-1][-1]