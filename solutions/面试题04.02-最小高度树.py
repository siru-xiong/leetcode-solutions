# Problem Id:  面试题 04.02
# Problem Name:  Minimum Height Tree LCCI, 最小高度树
# Problem Url:  https://leetcode-cn.com/problems/minimum-height-tree-lcci/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:
            n = len(nums)
            n = n // 2
            l = self.sortedArrayToBST(nums[:n])
            r = self.sortedArrayToBST(nums[(n+1):])
            res = TreeNode(nums[n])
            res.left = l
            res.right = r
            return res