# Problem Id:  139
# Problem Name:  Word Break, 单词拆分
# Problem Url:  https://leetcode-cn.com/problems/word-break/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(wordDict) == 0:
            return False
        t = [len(i) for i in wordDict]
        vmin = min(t)
        vmax = max(t)
        wordDict = set(wordDict)
        res = [False] * len(s)
        for i in range(len(s)):
            for j in range(vmin-1,vmax):
                temp = False
                if i - j >= 0:
                    temp = temp or s[(i-j):(i+1)] in wordDict
                if i - j - 1 >= 0:
                    temp = temp and res[i-j-1]
                res[i] = res[i] or temp
        return res[-1]
            