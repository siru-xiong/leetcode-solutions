# Problem Id:  1217
# Problem Name:  Minimum Cost to Move Chips to The Same Position, 玩筹码
# Problem Url:  https://leetcode-cn.com/problems/minimum-cost-to-move-chips-to-the-same-position/
# Problem Level:  Easy
 
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        odd = 0
        for k in position:
            if k % 2 == 0:
                even = even  + 1
            else:
                odd = odd + 1
        return min(even,odd)