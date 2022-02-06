# Problem Id:  45
# Problem Name:  Jump Game II, 跳跃游戏 II
# Problem Url:  https://leetcode-cn.com/problems/jump-game-ii/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res = 1
        left = 0
        right = nums[0]
        while len(nums)-1 > right:
            t = right
            for i in range(left,right+1):
                right = max(right,i+nums[i])
            left = t
            res = res + 1
        return res

