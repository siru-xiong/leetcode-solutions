# Problem Id:  810
# Problem Name:  Chalkboard XOR Game, 黑板异或游戏
# Problem Url:  https://leetcode-cn.com/problems/chalkboard-xor-game/
# Problem Level:  Hard
# Language:  Python3
 
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        re = 0
        for i in nums:
            re ^= i
        if re == 0:
            return True
        else:
            return len(nums) % 2 == 0