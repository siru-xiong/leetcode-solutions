# Problem Id:  416
# Problem Name:  Partition Equal Subset Sum, 分割等和子集
# Problem Url:  https://leetcode-cn.com/problems/partition-equal-subset-sum/
# Problem Level:  Medium
 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        vsum = sum(nums)
        if vsum % 2 != 0:
            return False
        else:
            vsum = int(vsum / 2)
        res = [False] * (vsum + 1)
        if nums[0] <= vsum:
            res[nums[0]] = True
        for k in range(1,len(nums)):
            for j in range(vsum,-1,-1):
                if j-nums[k] >= 0:
                    res[j] = res[j] or res[j-nums[k]]
        return res[vsum]