# Problem Id:  1561
# Problem Name:  Maximum Number of Coins You Can Get, 你可以获得的最大硬币数目
# Problem Url:  https://leetcode-cn.com/problems/maximum-number-of-coins-you-can-get/
# Problem Level:  Medium
 
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3
        i = 2
        j = 0
        res = 0
        while j < n:
            res = res + piles[-i]
            i = i + 2
            j = j + 1
        return res
        