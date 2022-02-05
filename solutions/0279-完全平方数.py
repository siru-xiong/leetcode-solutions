# Problem Id:  279
# Problem Name:  Perfect Squares, 完全平方数
# Problem Url:  https://leetcode-cn.com/problems/perfect-squares/
# Problem Level:  Medium
 
class Solution:
    def numSquares(self, n: int) -> int:
        temp = []
        for i in range(1,101):
            temp.append(i*i)
        temp = set(temp)
        ct = {}
        def nums(n):
            if n == 1:
                ct[n] = 1
            else:
                if n in temp:
                    ct[n] = 1
                else:
                    res = float('inf')
                    for i in temp:
                        if i < n:
                            res = min(res,1+ct[n-i])
                    ct[n] = res
        for i in range(1,n+1):
            nums(i)
        return ct[n]