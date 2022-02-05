# Problem Id:  349
# Problem Name:  Intersection of Two Arrays, 两个数组的交集
# Problem Url:  https://leetcode-cn.com/problems/intersection-of-two-arrays/
# Problem Level:  Easy
 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))