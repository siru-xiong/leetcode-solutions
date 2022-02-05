# Problem Id:  350
# Problem Name:  Intersection of Two Arrays II, 两个数组的交集 II
# Problem Url:  https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/
# Problem Level:  Easy
 
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        result = []
        for i in range(len(nums1)):
            count[nums1[i]] = count.get(nums1[i],0) + 1
        for j in range(len(nums2)):
            if count.get(nums2[j],0) != 0:
                result.append(nums2[j])
                count[nums2[j]] = count[nums2[j]] - 1
        return result