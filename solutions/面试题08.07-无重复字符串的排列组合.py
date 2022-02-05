# Problem Id:  面试题 08.07
# Problem Name:  Permutation I LCCI, 无重复字符串的排列组合
# Problem Url:  https://leetcode-cn.com/problems/permutation-i-lcci/
# Problem Level:  Medium
 
class Solution:
    def permutation(self, s: str) -> List[str]:
        if len(s) == 1:
            return [s]
        elif len(s) == 2:
            return [s,s[::-1]]
        else:
            r = self.permutation(s[1:])
            res = []
            for i in r:
                for j in range(len(i)+1):
                    res.append(i[:j]+s[0]+i[j:])
            return res