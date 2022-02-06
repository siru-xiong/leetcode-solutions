# Problem Id:  242
# Problem Name:  Valid Anagram, 有效的字母异位词
# Problem Url:  https://leetcode-cn.com/problems/valid-anagram/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            vdict = {}
            for i in range(len(s)):
                vdict[s[i]] = vdict.get(s[i],0) + 1
            for j in range(len(t)):
                vdict[t[j]] = vdict.get(t[j],0) - 1
            return len(set(vdict.values())) <= 1