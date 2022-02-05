# Problem Id:  643
# Problem Name:  Maximum Average Subarray I, 子数组最大平均数 I
# Problem Url:  https://leetcode-cn.com/problems/maximum-average-subarray-i/
# Problem Level:  Easy
 
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        value = sum(nums[0:k])
        vmax = value
        for i in range(1,len(nums)-k+1):
            value = value - nums[i-1] + nums[i+k-1]
            if value > vmax:
                vmax = value
        return vmax / k
