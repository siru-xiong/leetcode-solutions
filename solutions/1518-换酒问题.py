# Problem Id:  1518
# Problem Name:  Water Bottles, 换酒问题
# Problem Url:  https://leetcode-cn.com/problems/water-bottles/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles
        while numBottles >= numExchange:
            count = count + numBottles // numExchange
            numBottles = (numBottles // numExchange) + (numBottles % numExchange)
        return count