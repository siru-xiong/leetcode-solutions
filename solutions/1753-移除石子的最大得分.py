# Problem Id:  1753
# Problem Name:  Maximum Score From Removing Stones, 移除石子的最大得分
# Problem Url:  https://leetcode-cn.com/problems/maximum-score-from-removing-stones/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        res = 0 
        a , b , c = min(a,b,c) , a+b+c-min(a,b,c)-max(a,b,c) , max(a,b,c)
        if c - b >= a:
            return a + b
        else:
            res = c - b
            a = a - (c - b)
            res = res + a
            c = b

            b = b - (a // 2)
            c = c - (a // 2)
            if a % 2 == 1:
                b = b - 1

            return res + min(b,c)
