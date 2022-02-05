# Problem Id:  88
# Problem Name:  Merge Sorted Array, 合并两个有序数组
# Problem Url:  https://leetcode-cn.com/problems/merge-sorted-array/
# Problem Level:  Easy
 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0 and n!=0:
            nums1[:] = []
            nums1[:] = nums2[0:]
        if n != 0 and m!=0:
            nums1_copy = nums1[:m]
            nums1[:] = []
            i = 0
            j = 0
            while True:
                if nums1_copy[i] > nums2[j]:
                    nums1.append(nums2[j])
                    j = j + 1
                else:
                    nums1.append(nums1_copy[i])
                    i = i + 1
                if i == m or j ==n:
                    break
            if i < m:
                nums1[i+j:] = nums1_copy[i:]
            if j < n:
                nums1[i+j:] = nums2[j:]