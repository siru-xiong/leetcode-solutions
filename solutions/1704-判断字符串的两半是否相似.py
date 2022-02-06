# Problem Id:  1704
# Problem Name:  Determine if String Halves Are Alike, 判断字符串的两半是否相似
# Problem Url:  https://leetcode-cn.com/problems/determine-if-string-halves-are-alike/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s) // 2
        a = s[:l]
        b = s[l:]
        x = 0
        y = 0
        v = set(['a','e','i','o','u','A','E','I','O','U'])
        for i in range(l):
            if a[i] in v:
                x += 1
            if b[i] in v:
                y += 1
        return x == y
