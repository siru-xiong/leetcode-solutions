# Problem Id:  1137
# Problem Name:  N-th Tribonacci Number, 第 N 个泰波那契数
# Problem Url:  https://leetcode-cn.com/problems/n-th-tribonacci-number/
# Problem Level:  Easy
 
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            result = [0] * (n+1)
            result[1] = 1
            result[2] = 1
            for i in range(3,n+1):
                result[i] = result[i-1] + result[i-2] + result[i-3]
            return result[-1]