# Problem Id:  914
# Problem Name:  X of a Kind in a Deck of Cards, 卡牌分组
# Problem Url:  https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from math import gcd
        count = {}
        for i in range(len(deck)):
            count[deck[i]] = count.get(deck[i], 0) + 1
        count = count.values()
        return reduce(gcd, count) >= 2