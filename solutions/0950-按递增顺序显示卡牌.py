# Problem Id:  950
# Problem Name:  Reveal Cards In Increasing Order, 按递增顺序显示卡牌
# Problem Url:  https://leetcode-cn.com/problems/reveal-cards-in-increasing-order/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        rs = list(range(len(deck)))
        t = []
        while True:
            t.append(rs[0])
            del rs[0]
            if len(rs) == 0:
                break
            else:
                rs = rs[1:] + [rs[0]]
        deck.sort()
        res = [0] * len(deck)
        for i in range(len(deck)):
            res[t[i]] = deck[i]
        return res
