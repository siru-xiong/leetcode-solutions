# Problem Id:  965
# Problem Name:  Univalued Binary Tree, 单值二叉树
# Problem Url:  https://leetcode-cn.com/problems/univalued-binary-tree/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def equal(self, root:TreeNode, k) -> bool:
        if not root:
            return True
        elif root.val != k:
            return False
        else:
            return self.equal(root.left,k) and self.equal(root.right,k)

    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.equal(root,root.val)