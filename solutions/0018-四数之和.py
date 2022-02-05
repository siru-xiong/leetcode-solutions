# Problem Id:  18
# Problem Name:  4Sum, 四数之和
# Problem Url:  https://leetcode-cn.com/problems/4sum/
# Problem Level:  Medium
 
class Solution:
    def twosum(self, nums: List[int], target:int) -> List[List[int]]:
        if len(nums) <= 1:
            return []
        else:
            i = 0
            j = len(nums)-1
            res = []
            while j > i:
                if nums[i] + nums[j] < target:
                    i = i + 1
                elif nums[i] + nums[j] > target:
                    j = j - 1
                else:
                    res.append([nums[i],nums[j]])
                    i = i + 1
                    j = j - 1
            return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                t = self.twosum(nums[(j+1):],target-nums[i]-nums[j])
                for k in t:
                    res.append([nums[i],nums[j],k[0],k[1]])
        return [list(j) for j in set([tuple(i) for i in res])]
