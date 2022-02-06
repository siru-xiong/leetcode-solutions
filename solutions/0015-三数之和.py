# Problem Id:  15
# Problem Name:  3Sum, 三数之和
# Problem Url:  https://leetcode-cn.com/problems/3sum/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        last = float('inf')
        for i in range(len(nums)-2):
            if nums[i] == last:
                continue
            goal = -nums[i]
            left = i + 1
            right = len(nums)-1
            last2 = float('inf')
            while left<right:
                if nums[left]+nums[right] < goal:
                    left = left + 1
                elif nums[left]+nums[right]>goal:
                    right = right -1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    while left+1 <= right and nums[left+1] == nums[left]:
                        left = left + 1
                    left = left + 1
                    right = right - 1          
            last = nums[i]
        return res