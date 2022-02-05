# Problem Id:  剑指 Offer 63
# Problem Name:  股票的最大利润  LCOF, 股票的最大利润
# Problem Url:  https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/
# Problem Level:  Medium
 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        elif len(prices) == 2:
            return max(0,prices[1]-prices[0])
        else:
            vmin = min(prices[0],prices[1])
            res = [0,max(0,prices[1]-prices[0])]
            for i in range(2,len(prices)):
                res.append(max(res[-1],max(prices[i]-vmin,0)))
                vmin = min(vmin,prices[i])
            return res[-1]
            


