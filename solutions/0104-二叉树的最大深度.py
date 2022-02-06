# Problem Id:  104
# Problem Name:  Maximum Depth of Binary Tree, 二叉树的最大深度
# Problem Url:  https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))