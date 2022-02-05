# Problem Id:  1175
# Problem Name:  Prime Arrangements, 质数排列
# Problem Url:  https://leetcode-cn.com/problems/prime-arrangements/
# Problem Level:  Easy
 
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        p = 0
        for i in prime:
            if i <= n:
                p = p + 1
            else:
                break
        np = n - p
        if n == 1:
            return 1
        else:
            res = 1
            for i in range(1,p+1):
                res = (res * i) % 1000000007
            for i in range(1,np+1):
                res = (res * i) % 1000000007
            return res