# Problem Id:  122
# Problem Name:  Best Time to Buy and Sell Stock II, 买卖股票的最佳时机 II
# Problem Url:  https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1,len(prices)):
            if prices[i] - prices[i-1] > 0:
                result = result + prices[i] - prices[i-1]
        return result
