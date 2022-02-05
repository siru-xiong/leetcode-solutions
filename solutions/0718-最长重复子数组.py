# Problem Id:  718
# Problem Name:  Maximum Length of Repeated Subarray, 最长重复子数组
# Problem Url:  https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
# Problem Level:  Medium
 
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        res = []
        for i in range(m):
            res.append([0]*n)
        if nums1[0] == nums2[0]:
            res[0][0] = 1
        for j in range(1,n):
            if nums2[j] == nums1[0]:
                res[0][j] = 1
        for i in range(1,m):
            if nums1[i] == nums2[0]:
                res[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                if nums1[i] == nums2[j]:
                    res[i][j] = res[i-1][j-1] + 1
        return max([max(i) for i in res])