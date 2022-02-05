# Problem Id:  面试题 08.03
# Problem Name:  Magic Index LCCI, 魔术索引
# Problem Url:  https://leetcode-cn.com/problems/magic-index-lcci/
# Problem Level:  Easy
 
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == i:
                return i
        return -1