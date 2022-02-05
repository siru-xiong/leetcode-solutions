# Problem Id:  228
# Problem Name:  Summary Ranges, 汇总区间
# Problem Url:  https://leetcode-cn.com/problems/summary-ranges/
# Problem Level:  Easy
 
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        else:
            result = []
            left = 0
            right = 0
            for i in range(1,len(nums)):
                if nums[i] == (nums[right] + 1):
                    right = right + 1
                else:
                    if left == right:
                        result = result + [str(nums[left])]
                        left = i
                        right = i
                    else:
                        result = result + [str(nums[left])+'->'+str(nums[right])]
                        left = i
                        right = i
            if left == right:
                result = result + [str(nums[left])]
            else:
                result = result + [str(nums[left])+'->'+str(nums[right])]
            return result
