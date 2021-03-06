# Problem Id:  814
# Problem Name:  Binary Tree Pruning, 二叉树剪枝
# Problem Url:  https://leetcode-cn.com/problems/binary-tree-pruning/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        else:
            root.left,root.right = self.pruneTree(root.left),self.pruneTree(root.right)
            if root.val == 0 and not root.left and not root.right:
                return None
            else:
                return root