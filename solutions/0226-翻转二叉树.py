# Problem Id:  226
# Problem Name:  Invert Binary Tree, 翻转二叉树
# Problem Url:  https://leetcode-cn.com/problems/invert-binary-tree/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        else:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root