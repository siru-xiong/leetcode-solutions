# Problem Id:  389
# Problem Name:  Find the Difference, 找不同
# Problem Url:  https://leetcode-cn.com/problems/find-the-difference/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}
        result = -1
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0) + 1
        for i in range(len(t)):
            if count.get(t[i],0) == 0:
                result = t[i]
                break
            else:
                count[t[i]] = count[t[i]] - 1
        return result
             
