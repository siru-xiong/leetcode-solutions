# Problem Id:  剑指 Offer 38
# Problem Name:  字符串的排列  LCOF, 字符串的排列
# Problem Url:  https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def permutation(self, s: str) -> List[str]:
        if len(s) == 1:
            return [s]
        elif len(s) == 2:
            if s[0] == s[1]:
                return [s]
            else:
                return [s,s[::-1]]
        else:
            r = self.permutation(s[1:])
            res = []
            for i in r:
                for j in range(len(i)+1):
                    res.append(i[:j]+s[0]+i[j:])
            return list(set(res))