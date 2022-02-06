# Problem Id:  49
# Problem Name:  Group Anagrams, 字母异位词分组
# Problem Url:  https://leetcode-cn.com/problems/group-anagrams/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        def myfun(s):
            ct = {}
            for j in s:
                ct[j] = ct.get(j,0)+1
            ct = tuple([ct.get(i,0) for i in temp])
            return ct
        mydic = {}
        for i in strs:
            tp = myfun(i)
            if tp not in mydic:
                mydic[tp] = [i]
            else:
                mydic[tp].append(i)

        res = []
        for i in mydic:
            res.append(mydic[i])
        return res
        