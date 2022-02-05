# Problem Id:  276
# Problem Name:  Paint Fence, 栅栏涂色
# Problem Url:  https://leetcode-cn.com/problems/paint-fence/
# Problem Level:  Medium
 
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return k
        elif n == 2:
            return k*k
        else:
            dp = [0] * n
            dp[0] = k
            dp[1] = k*k
            for i in range(2,n):
                dp[i] = dp[i-1]*(k-1) + dp[i-2]*(k-1)
            return dp[-1]