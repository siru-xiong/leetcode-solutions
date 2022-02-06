# Problem Id:  1431
# Problem Name:  Kids With the Greatest Number of Candies, 拥有最多糖果的孩子
# Problem Url:  https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        i = max(candies)
        return [j+extraCandies >= i for j in candies]