# Problem Id:  264
# Problem Name:  Ugly Number II, 丑数 II
# Problem Url:  https://leetcode-cn.com/problems/ugly-number-ii/
# Problem Level:  Medium
 
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        a,b,c = 0,0,0
        for i in range(n-1):
            res.append(min(res[a]*2,res[b]*3,res[c]*5))
            if res[-1] == res[a]*2:
                a += 1
            if res[-1] == res[b]*3:
                b += 1
            if res[-1] == res[c]*5:
                c += 1
        return res[-1]