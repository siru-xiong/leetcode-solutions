# Problem Id:  518
# Problem Name:  Coin Change 2, 零钱兑换 II
# Problem Url:  https://leetcode-cn.com/problems/coin-change-2/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        res = [0] * (amount+1)
        res[0] = 1
        for i in coins:
            for j in range(1,amount+1):
                if j >= i:
                    res[j] += res[j-i]
        return res[-1]