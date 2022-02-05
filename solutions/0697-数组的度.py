# Problem Id:  697
# Problem Name:  Degree of an Array, 数组的度
# Problem Url:  https://leetcode-cn.com/problems/degree-of-an-array/
# Problem Level:  Easy
 
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left = {}
        right = {}
        count = {}
        for i,x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
        result = len(nums)
        degree = max(count.values())

        for x in count:
            if count[x] == degree:
                result = min(result,right[x]-left[x]+1)   
        return result