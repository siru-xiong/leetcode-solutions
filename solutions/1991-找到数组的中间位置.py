# Problem Id:  1991
# Problem Name:  Find the Middle Index in Array, 找到数组的中间位置
# Problem Url:  https://leetcode-cn.com/problems/find-the-middle-index-in-array/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0
        else:
            left = 0
            right = sum(nums[1:])
            for i in range(len(nums)-1):
                if left == right:
                    return i
                else:
                    left += nums[i]
                    right -= nums[i+1]
            if left == right:
                return len(nums)-1
            else:
                return -1