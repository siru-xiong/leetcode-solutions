# Problem Id:  111
# Problem Name:  Minimum Depth of Binary Tree, 二叉树的最小深度
# Problem Url:  https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif root.right and not root.left:
            return 1 + self.minDepth(root.right)
        elif root.left and not root.right:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left),self.minDepth(root.right))