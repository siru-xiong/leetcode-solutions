# Problem Id:  90
# Problem Name:  Subsets II, 子集 II
# Problem Url:  https://leetcode-cn.com/problems/subsets-ii/
# Problem Level:  Medium
 
class Solution:
    def s(self, nums: List[int]) -> List[List[int]]:
        if len(set(nums)) == 1:
            x = len(nums)
            return [[]] + [[nums[0]] * i for i in range(1,x+1) ]
        else:
            s = nums[0]
            for i in range(len(nums)):
                if nums[i] == s:
                    e = i
                else:
                    break
            x = e + 1
            a = [[]] + [[s] * i for i in range(1,x+1)]
            b = self.s(nums[(e+1):])
            return [i+j for i in a for j in b]


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.s(nums)