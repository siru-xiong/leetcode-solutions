# Problem Id:  1716
# Problem Name:  Calculate Money in Leetcode Bank, 计算力扣银行的钱
# Problem Url:  https://leetcode-cn.com/problems/calculate-money-in-leetcode-bank/
# Problem Level:  Easy
 
class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        for i in range(1,n+1):
            week = ((i-1) // 7) + 1
            day = ((i-1) % 7) + 1
            res = res + week + day - 1
        return res
