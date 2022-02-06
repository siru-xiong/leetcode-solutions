# Problem Id:  4
# Problem Name:  Median of Two Sorted Arrays, 寻找两个正序数组的中位数
# Problem Url:  https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
# Problem Level:  Hard
# Language:  Python3
 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2)//2 - 1] + nums2[len(nums2)//2])/2
            else:
                return nums2[len(nums2)//2]
        if len(nums2) == 0:
            if len(nums1) % 2 == 0:
                return (nums1[len(nums1)//2 - 1] + nums1[len(nums1)//2])/2
            else:
                return nums1[len(nums1)//2]  
        len1 = len(nums1)
        len2 = len(nums2)
        s = (len1 + len2) // 2
        nums1.append(float("inf"))
        nums2.append(float("inf"))
        i = 0
        j = 0
        while True:
            if i+j == s-1:
                break
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                j += 1
        if (len1+len2) % 2 == 0:
            res = 0
            if nums1[i] <= nums2[j]:
                res += nums1[i]
                i += 1
            else:
                res += nums2[j]
                j += 1
            if nums1[i] <= nums2[j]:
                res += nums1[i]
                i += 1
            else:
                res += nums2[j]
                j += 1
            return res/2.0
        else:
            res = 0
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                j += 1
            if nums1[i] <= nums2[j]:
                return nums1[i]
            else:
                return nums2[j]

