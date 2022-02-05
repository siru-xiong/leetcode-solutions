# Problem Id:  剑指 Offer 55 - I
# Problem Name:  二叉树的深度 LCOF, 二叉树的深度
# Problem Url:  https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))