# Problem Id:  1011
# Problem Name:  Capacity To Ship Packages Within D Days, 在 D 天内送达包裹的能力
# Problem Url:  https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/
# Problem Level:  Medium
 
class Solution:
    def need(self, weights, cap):
        d = 0
        s = 0
        for i in weights:
            if s + i > cap:
                d += 1
                s = i
            else:
                s += i
        d += 1
        return d

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while r > l:
            mid = (l+r) // 2
            if self.need(weights,mid) <= days:
                r = mid
            else:
                l = mid + 1
        return l
