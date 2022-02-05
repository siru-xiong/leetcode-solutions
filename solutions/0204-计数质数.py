# Problem Id:  204
# Problem Name:  Count Primes, 计数质数
# Problem Url:  https://leetcode-cn.com/problems/count-primes/
# Problem Level:  Medium
 
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        else:
            result = []
            primes = list(range(n))
            for i in range(2,n):
                if primes[i] != -1:
                    result.append(primes[i])
                    j = i
                    while i*j<n:
                        primes[i*j] = -1
                        j = j + 1
            return len(result)
