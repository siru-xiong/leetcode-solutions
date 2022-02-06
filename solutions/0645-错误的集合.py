# Problem Id:  645
# Problem Name:  Set Mismatch, 错误的集合
# Problem Url:  https://leetcode-cn.com/problems/set-mismatch/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0) + 1
            if count[nums[i]] == 2:
                result.append(nums[i])
        for i in range(1,len(nums)+1):
            if i not in count:
                result.append(i)
                break
        return result