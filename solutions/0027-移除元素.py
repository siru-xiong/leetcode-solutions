# Problem Id:  27
# Problem Name:  Remove Element, 移除元素
# Problem Url:  https://leetcode-cn.com/problems/remove-element/
# Problem Level:  Easy
 
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        while True:
            if index < len(nums):
                if nums[index] == val:
                    del nums[index]
                else:
                    index = index + 1
            else:
                break
                
