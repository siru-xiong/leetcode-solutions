# Problem Id:  977
# Problem Name:  Squares of a Sorted Array, 有序数组的平方
# Problem Url:  https://leetcode-cn.com/problems/squares-of-a-sorted-array/
# Problem Level:  Easy
 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return [nums[i]*nums[i] for i in range(len(nums))]
        elif nums[-1] <= 0:
            return [nums[-i]*nums[-i] for i in range(1,len(nums)+1)]
        else:
            for k in range(len(nums)-1):
                if nums[k] <= 0 and nums[k+1] >= 0:
                    i = k
                    j = k + 1
                    break
            nums = [nums[i]*nums[i] for i in range(len(nums))]
            result = []
            while True:
                if nums[i] >= nums[j]:
                    result.append(nums[j])
                    j = j + 1
                else:
                    result.append(nums[i])
                    i = i - 1
                if i == -1 or j == len(nums):
                    break
            if i != -1:
                result = result + nums[i::-1]
            if j != len(nums):
                result = result + nums[j:]
            return result
