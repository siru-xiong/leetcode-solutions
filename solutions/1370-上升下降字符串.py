# Problem Id:  1370
# Problem Name:  Increasing Decreasing String, 上升下降字符串
# Problem Url:  https://leetcode-cn.com/problems/increasing-decreasing-string/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        s.sort()
        us = []
        for i in range(len(s)):
            if s[i] not in us:
                us.append(s[i])
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0)+1
        
        result = []

        while len(us)>0:
            i = 0
            while i<len(us):
                if count[us[i]] > 0:
                    result.append(us[i])
                    count[us[i]] = count[us[i]] - 1
                    i = i + 1
                else:
                    del us[i]

            i = -1
            while -i <= len(us):
                if count[us[i]] > 0:
                    result.append(us[i])
                    count[us[i]] = count[us[i]] - 1
                    i = i -1
                else:
                    del us[i]

        return ''.join(result)

            
        
