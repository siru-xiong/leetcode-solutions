# Problem Id:  1304
# Problem Name:  Find N Unique Integers Sum up to Zero, 和为零的N个唯一整数
# Problem Url:  https://leetcode-cn.com/problems/find-n-unique-integers-sum-up-to-zero/
# Problem Level:  Easy
 
class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            n = n // 2
            return list(range(-n,0)) + list(range(1,n+1))
        else:
            n = (n-1) // 2
            return list(range(-n,0)) + [0] + list(range(1,n+1))