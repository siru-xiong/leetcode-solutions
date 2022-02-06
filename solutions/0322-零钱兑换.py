# Problem Id:  322
# Problem Name:  Coin Change, 零钱兑换
# Problem Url:  https://leetcode-cn.com/problems/coin-change/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in coins:
            if i <= amount:
                dp[i] = 1
        for i in range(amount+1):
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1 