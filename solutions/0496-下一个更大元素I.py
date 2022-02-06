# Problem Id:  496
# Problem Name:  Next Greater Element I, 下一个更大元素 I
# Problem Url:  https://leetcode-cn.com/problems/next-greater-element-i/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ct = {}
        stack = []
        for i in nums2:
            if len(stack) == 0:
                stack.append(i)
            else:
                while len(stack) >= 1 and i > stack[-1]:
                    ct[stack[-1]] = i
                    del stack[-1]
                stack.append(i)
        while len(stack) >= 1:
            ct[stack[-1]] = -1
            del stack[-1]
        res = []
        for i in nums1:
            res.append(ct[i])
        return res