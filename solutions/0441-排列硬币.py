# Problem Id:  441
# Problem Name:  Arranging Coins, 排列硬币
# Problem Url:  https://leetcode-cn.com/problems/arranging-coins/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            left = 1
            right = n
            while right - left >= 2:
                med = int((left+right)/2)
                if med*(med+1) < 2*n:
                    left = med
                elif med*(med+1) > 2*n:
                    right = med
                else:
                    left = med
                    right = med
            if right == left:
                return left
            elif left*(left+1) == 2*n:
                return left
            elif right*(right+1) > 2*n:
                return left
            else:
                return right