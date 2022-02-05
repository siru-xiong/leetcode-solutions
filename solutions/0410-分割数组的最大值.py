# Problem Id:  410
# Problem Name:  Split Array Largest Sum, 分割数组的最大值
# Problem Url:  https://leetcode-cn.com/problems/split-array-largest-sum/
# Problem Level:  Hard
 
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        return self.shipWithinDays(nums,m)

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