# Problem Id:  163
# Problem Name:  Missing Ranges, 缺失的区间
# Problem Url:  https://leetcode-cn.com/problems/missing-ranges/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        nums = [lower] + nums + [upper]
        for i in range(1,len(nums)):
            left = nums[i-1] + 1
            right = nums[i] - 1
            if i == 1:
                left = left - 1
            if i == len(nums)-1:
                right = right + 1
            if right == left:
                res.append(str(right))
            elif right > left:
                res.append(str(left)+"->"+str(right))
        return res