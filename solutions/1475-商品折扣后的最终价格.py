# Problem Id:  1475
# Problem Name:  Final Prices With a Special Discount in a Shop, 商品折扣后的最终价格
# Problem Url:  https://leetcode-cn.com/problems/final-prices-with-a-special-discount-in-a-shop/
# Problem Level:  Easy
 
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ct = {}
        for i in range(len(prices)):
            if len(stack) == 0:
                stack.append(prices[i])
            elif prices[i] > stack[-1]:
                stack.append(prices[i])
            else:
                j = 0
                while True:
                    if stack[j] < prices[i]:
                        j = j + 1
                    else:
                        if stack[j] not in ct:
                            ct[stack[j]] = [stack[j]-prices[i]]
                        else:
                            ct[stack[j]].append(stack[j]-prices[i])
                        del stack[j]
                    if len(stack) == 0 or j >= len(stack):
                        break
                stack.append(prices[i])
        for i in range(len(stack)):
            if stack[i] not in ct:
                ct[stack[i]] = [stack[i]]
            else:
                ct[stack[i]].append(stack[i])
        res = []
        for i in range(len(prices)):
            res.append(ct[prices[i]][0])
            del ct[prices[i]][0]
        return res



