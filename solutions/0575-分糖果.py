# Problem Id:  575
# Problem Name:  Distribute Candies, 分糖果
# Problem Url:  https://leetcode-cn.com/problems/distribute-candies/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)),int(len(candyType)/2))



