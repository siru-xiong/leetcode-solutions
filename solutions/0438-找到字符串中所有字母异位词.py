# Problem Id:  438
# Problem Name:  Find All Anagrams in a String, 找到字符串中所有字母异位词
# Problem Url:  https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        temp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        lp = len(p)
        def myfun(s):
            ct = {}
            for j in s:
                ct[j] = ct.get(j,0)+1
            return ct
        p = tuple([myfun(p).get(i,0) for i in temp])
        record = {}
        record[p] = '0'
        res = []
        if len(s) < lp:
            return []
        else:
            start = myfun(s[0:lp])
            if tuple([start.get(i,0) for i in temp]) in record:
                res.append(0)
            for i in range(lp,len(s)):
                start[s[i-lp]] -= 1
                start[s[i]] = start.get(s[i],0)+1
                if tuple([start.get(i,0) for i in temp]) in record:
                    res.append(i-lp+1)
            return res
