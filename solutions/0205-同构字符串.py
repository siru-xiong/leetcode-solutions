# Problem Id:  205
# Problem Name:  Isomorphic Strings, 同构字符串
# Problem Url:  https://leetcode-cn.com/problems/isomorphic-strings/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        vdict = {}
        result = True
        for i in range(len(s)):
            if s[i] not in vdict and t[i] not in vdict.values():
                vdict[s[i]] = t[i]
            elif s[i] in vdict and vdict[s[i]] == t[i]:
                pass
            else:
                result = False
        return result