# Problem Id:  1636
# Problem Name:  Sort Array by Increasing Frequency, 按照频率将数组升序排序
# Problem Url:  https://leetcode-cn.com/problems/sort-array-by-increasing-frequency/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ct = {}
        for i in range(len(nums)):
            ct[nums[i]] = ct.get(nums[i],0) + 1
        
        def cp(x):
            return (ct[x],-x)
        
        return sorted(nums,key=cp)