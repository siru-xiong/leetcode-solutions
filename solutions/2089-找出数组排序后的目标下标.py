# Problem Id:  2089
# Problem Name:  Find Target Indices After Sorting Array, 找出数组排序后的目标下标
# Problem Url:  https://leetcode-cn.com/problems/find-target-indices-after-sorting-array/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        a = sum([i<target for i in nums])
        b = sum([i==target for i in nums])
        return list(range(a,a+b))