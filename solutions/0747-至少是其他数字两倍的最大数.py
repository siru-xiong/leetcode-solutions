# Problem Id:  747
# Problem Name:  Largest Number At Least Twice of Others, 至少是其他数字两倍的最大数
# Problem Url:  https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/
# Problem Level:  Easy
 
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            vmax = [float('-inf'),float('-inf')]
            for i in range(len(nums)):
                if nums[i] > vmax[0]:
                    index = i
                    vmax = [nums[i],vmax[0]]
                elif nums[i] > vmax[1]:
                    vmax = [vmax[0],nums[i]]
            if vmax[0] >= 2 * vmax[1]:
                return index
            else:
                return -1
                