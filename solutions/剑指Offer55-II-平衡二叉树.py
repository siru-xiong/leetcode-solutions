# Problem Id:  剑指 Offer 55 - II
# Problem Name:  平衡二叉树 LCOF, 平衡二叉树
# Problem Url:  https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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