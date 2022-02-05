# Problem Id:  309
# Problem Name:  Best Time to Buy and Sell Stock with Cooldown, 最佳买卖股票时机含冷冻期
# Problem Url:  https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# Problem Level:  Medium
 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        elif len(prices) == 2:
            return max(0,prices[1]-prices[0])
        else:
            res = [0,0,0,max(0,prices[1]-prices[0])]
            for i in range(2,len(prices)):
                
                res.append(max(max([res[k] + prices[i] - prices[k] for k in range(i+1)]),res[-1]))
            return res[-1]
