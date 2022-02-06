# Problem Id:  1855
# Problem Name:  Maximum Distance Between a Pair of Values, 下标对中的最大距离
# Problem Url:  https://leetcode-cn.com/problems/maximum-distance-between-a-pair-of-values/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        res = 0
        for i in range(len(nums1)):
            while j+1 < len(nums2) and nums2[j+1] >= nums1[i]:
                j += 1
            res = max(res,j-i)
        return res
             