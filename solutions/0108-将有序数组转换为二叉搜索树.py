# Problem Id:  108
# Problem Name:  Convert Sorted Array to Binary Search Tree, 将有序数组转换为二叉搜索树
# Problem Url:  https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(val=nums[0])
        elif len(nums) == 2:
            return TreeNode(val=nums[1],left=TreeNode(val=nums[0]))
        else:
            mid = int(len(nums)/2)
            return TreeNode(val=nums[mid],left=self.sortedArrayToBST(nums[0:mid]),right=self.sortedArrayToBST(nums[(mid+1):]))