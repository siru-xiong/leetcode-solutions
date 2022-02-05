# Problem Id:  14
# Problem Name:  Longest Common Prefix, 最长公共前缀
# Problem Url:  https://leetcode-cn.com/problems/longest-common-prefix/
# Problem Level:  Easy
 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        else:
            result = ""
            i = 0
            while True:
                temp = 1
                for j in range(len(strs)):
                    if i + 1 > len(strs[j]) or strs[j][i] != strs[0][i]:
                        temp = 0
                        break
            
                if temp == 0:
                    break
                else:
                    result = result + strs[0][i]
                    i = i + 1
            return result