# Problem Id:  131
# Problem Name:  Palindrome Partitioning, 分割回文串
# Problem Url:  https://leetcode-cn.com/problems/palindrome-partitioning/
# Problem Level:  Medium
 
class Solution:
    def t(self, s:str):
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return [[]]
        elif len(s) == 1:
            return [[s[0]]]
        else:
            i = 0
            q = [p for p in range(1,len(s)+1) if self.t(s[:p])==1]
            res = []
            for x in q:
                res = res + [[s[:x]]+y for y in self.partition(s[x:])]
            return res

        
