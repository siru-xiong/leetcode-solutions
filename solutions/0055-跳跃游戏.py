# Problem Id:  55
# Problem Name:  Jump Game, 跳跃游戏
# Problem Url:  https://leetcode-cn.com/problems/jump-game/
# Problem Level:  Medium
 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = 0
        for i in range(len(nums)):
            if i > r:
                return False
            else:
                r = max(r,i+nums[i])
        return r >= len(nums)-1
