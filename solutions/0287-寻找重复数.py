# Problem Id:  287
# Problem Name:  Find the Duplicate Number, 寻找重复数
# Problem Url:  https://leetcode-cn.com/problems/find-the-duplicate-number/
# Problem Level:  Medium
 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = 0
        while True:
            i = nums[i]
            j = nums[nums[j]]
            if i == j:
                break
        i = 0
        while nums[i] != nums[j]:
            i = nums[i]
            j = nums[j]
        return nums[i]