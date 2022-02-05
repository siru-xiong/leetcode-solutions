# Problem Id:  942
# Problem Name:  DI String Match, 增减字符串匹配
# Problem Url:  https://leetcode-cn.com/problems/di-string-match/
# Problem Level:  Easy
 
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        vmax = 0
        vmin = 0
        res = [0] * (len(S)+1)
        for i in range(len(S)):
            if S[i] == 'I':
                res[i+1] = vmax+1
                vmax = res[i+1]
            else:
                res[i+1] = vmin-1
                vmin = res[i+1]
        minres = min(res)
        res = [i-minres for i in res]
        return res