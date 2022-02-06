# Problem Id:  剑指 Offer 51
# Problem Name:  数组中的逆序对  LCOF, 数组中的逆序对
# Problem Url:  https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
# Problem Level:  Hard
# Language:  Python3
 
class Solution:
    def rev(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return (0,nums)
        elif len(nums) == 2:
            if nums[0] <= nums[1]:
                return (0,nums)
            else:
                return (1,[nums[1],nums[0]])
        else:
            mid = len(nums) // 2
            left = self.rev(nums[:mid])
            right = self.rev(nums[mid:])
            m = self.merge(left[1],right[1])
            return (left[0] + right[0] + m[0],m[1])
    
    def merge(self,nums1,nums2):
        i = 0
        j = 0
        res = 0
        reslist = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                reslist.append(nums1[i])
                i = i + 1
            else:
                reslist.append(nums2[j])
                res = res + len(nums1)-i
                j = j + 1
        if i < len(nums1):
            reslist = reslist + nums1[i:]
        if j < len(nums2):
            reslist = reslist + nums2[j:]
        return (res,reslist)

    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        return self.rev(nums)[0]

