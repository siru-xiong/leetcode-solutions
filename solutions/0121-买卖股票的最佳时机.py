# Problem Id:  121
# Problem Name:  Best Time to Buy and Sell Stock, 买卖股票的最佳时机
# Problem Url:  https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0]=0
        dp[0][1]=-prices[0]
        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1]=max(-prices[i],dp[i-1][1])
        return dp[-1][0]