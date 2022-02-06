# Problem Id:  455
# Problem Name:  Assign Cookies, 分发饼干
# Problem Url:  https://leetcode-cn.com/problems/assign-cookies/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0
        else:
            g.sort()
            s.sort()
            i = len(g)-1
            j = len(s)-1
            count = 0
            while i >= 0 and j >= 0:
                if s[j] >= g[i]:
                    count = count + 1
                    j = j -1
                    i = i -1
                else:
                    i = i - 1
            return count