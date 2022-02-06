# Problem Id:  868
# Problem Name:  Binary Gap, 二进制间距
# Problem Url:  https://leetcode-cn.com/problems/binary-gap/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def binaryGap(self, n: int) -> int:
        c = 1
        t = 0
        while True:
            c = c * 2
            t = t + 1
            if c > n:
                c = c // 2
                break
        res = []
        for i in range(t):
            res.append(n // c)
            n = n % c
            c = c // 2
        dist = 0
        start = 0
        for i in range(1,len(res)):
            if res[i] == 1:
                dist = max(dist,i-start)
                start = i
        return dist


