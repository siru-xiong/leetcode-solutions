# Problem Id:  面试题 17.09
# Problem Name:  Get Kth Magic Number LCCI, 第 k 个数
# Problem Url:  https://leetcode-cn.com/problems/get-kth-magic-number-lcci/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        res = [1]
        a = 0
        b = 0
        c = 0
        for i in range(k-1):
            res.append(min(res[a]*3,res[b]*5,res[c]*7))
            if res[-1] == res[a] * 3:
                a += 1
            if res[-1] == res[b] * 5:
                b += 1
            if res[-1] == res[c] * 7:
                c += 1
        return res[-1]