# Problem Id:  292
# Problem Name:  Nim Game, Nim 游戏
# Problem Url:  https://leetcode-cn.com/problems/nim-game/
# Problem Level:  Easy
 
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 >= 1

