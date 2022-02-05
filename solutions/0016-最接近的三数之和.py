# Problem Id:  16
# Problem Name:  3Sum Closest, 最接近的三数之和
# Problem Url:  https://leetcode-cn.com/problems/3sum-closest/
# Problem Level:  Medium
 
class Solution:
    def tc(self, nums: List[int], target: int):
        res = [float('inf'),-1]
        i = 0
        j = len(nums)-1
        while j > i:
            if abs(nums[i] + nums[j] - target) < res[0]:
                res[0] = abs(nums[i] + nums[j] - target)
                res[1] = nums[i] + nums[j]
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                res = [0,target]
                break
        return res

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = [float('inf'),-1]
        for i in range(len(nums)-2):
            t = self.tc(nums[(i+1):],target-nums[i])
            if t[0] < res[0]:
                res = [t[0],t[1]+nums[i]]
        return res[1]
