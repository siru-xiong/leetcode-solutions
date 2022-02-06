# Problem Id:  724
# Problem Name:  Find Pivot Index, 寻找数组的中心下标
# Problem Url:  https://leetcode-cn.com/problems/find-pivot-index/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0
        else:
            left = 0
            right = sum(nums[1:])
            result = -1
            for i in range(len(nums)-1):
                if left == right:
                    result = i
                    break
                else:
                    left = left + nums[i]
                    right = right - nums[i+1]
            if left == right and result!= -1:
                return result
            elif left == right and result == -1:
                return len(nums)-1
            else:
                return -1