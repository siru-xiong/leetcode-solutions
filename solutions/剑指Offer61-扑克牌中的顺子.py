# Problem Id:  剑指 Offer 61
# Problem Name:  扑克牌中的顺子  LCOF, 扑克牌中的顺子
# Problem Url:  https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        j = 0
        nums.sort()
        for i in range(4):
            if nums[i] == 0:
                j += 1
            elif nums[i] == nums[i + 1]:
                return False
        return nums[4] - nums[j] < 5