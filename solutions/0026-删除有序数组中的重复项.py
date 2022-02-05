# Problem Id:  26
# Problem Name:  Remove Duplicates from Sorted Array, 删除有序数组中的重复项
# Problem Url:  https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
# Problem Level:  Easy
 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        else:
            index = 0
            count = 1
            i = 1
            while True:
                if i < len(nums):
                    if nums[index] == nums[i]:
                        del nums[i]
                    else:
                        count = count + 1
                        index = i
                        i = i + 1
                else:
                    break
            
            return count

