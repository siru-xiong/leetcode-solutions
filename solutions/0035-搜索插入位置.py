# Problem Id:  35
# Problem Name:  Search Insert Position, 搜索插入位置
# Problem Url:  https://leetcode-cn.com/problems/search-insert-position/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        temp = -1
        for i in range(len(nums)):
            if nums[i] == target:
                result = i
                break
            elif nums[i] < target:
                temp = i
            elif nums[i] > target:
                if i == 0:
                    result = 0
                    break
                else:
                    result = temp + 1
                    break
        
        if temp == len(nums) - 1:
            return len(nums)
        else:
            return result



