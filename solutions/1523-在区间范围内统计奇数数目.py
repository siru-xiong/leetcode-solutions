# Problem Id:  1523
# Problem Name:  Count Odd Numbers in an Interval Range, 在区间范围内统计奇数数目
# Problem Url:  https://leetcode-cn.com/problems/count-odd-numbers-in-an-interval-range/
# Problem Level:  Easy
 
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 1 and high % 2 == 1:
            return ((high-low) // 2) + 1
        elif low % 2 == 1 and high % 2 == 0:
            return self.countOdds(low,high-1)
        elif low % 2 == 0 and high % 2 == 1:
            return self.countOdds(low+1,high)
        else:
            return self.countOdds(low+1,high-1)