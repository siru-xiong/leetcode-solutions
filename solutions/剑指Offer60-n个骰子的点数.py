# Problem Id:  剑指 Offer 60
# Problem Name:  n个骰子的点数  LCOF, n个骰子的点数
# Problem Url:  https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def comp(self,a,b):
        m = len(a)
        n = len(b)
        res = [0] * (m+n-1)
        for i in range(m+n-1):
            for j in range(i+1):
                if j < m and i-j < n:
                    res[i] += a[j]*b[i-j]
        return res

    def dicesProbability(self, n: int) -> List[float]:
        base = [1.0/6] * 6
        res = [1.0/6] * 6
        for i in range(n-1):
            res = self.comp(res,base)
        return res
