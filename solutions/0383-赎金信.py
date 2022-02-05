# Problem Id:  383
# Problem Name:  Ransom Note, 赎金信
# Problem Url:  https://leetcode-cn.com/problems/ransom-note/
# Problem Level:  Easy
 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = {}
        b = {}
        for i in ransomNote:
            a[i] = a.get(i,0) + 1
        for i in magazine:
            b[i] = b.get(i,0) + 1
        res = True
        for i in a:
            if a[i] > b.get(i,0):
                res = False
                break
        return res