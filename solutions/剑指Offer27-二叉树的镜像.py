# Problem Id:  剑指 Offer 27
# Problem Name:  二叉树的镜像  LCOF, 二叉树的镜像
# Problem Url:  https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        else:
            root.left , root.right = self.mirrorTree(root.right) , self.mirrorTree(root.left)
            return root