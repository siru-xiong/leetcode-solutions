# Problem Id:  1672
# Problem Name:  Richest Customer Wealth, 最富有客户的资产总量
# Problem Url:  https://leetcode-cn.com/problems/richest-customer-wealth/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(i) for i in accounts])