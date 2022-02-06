# Problem Id:  110
# Problem Name:  Balanced Binary Tree, 平衡二叉树
# Problem Url:  https://leetcode-cn.com/problems/balanced-binary-tree/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.depth(root.left),self.depth(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        else:
            result1 = self.isBalanced(root.left) and self.isBalanced(root.right)
            result2 = abs(self.depth(root.left) - self.depth(root.right)) <= 1
            return result1 and result2