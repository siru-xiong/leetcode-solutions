# Problem Id:  剑指 Offer 28
# Problem Name:  对称的二叉树  LCOF, 对称的二叉树
# Problem Url:  https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(self, r1: TreeNode, r2: TreeNode) -> bool:
        if not r1 and not r2:
            return True
        elif not r1 or not r2:
            return False
        else:
            return r1.val == r2.val and self.check(r1.left,r2.right) and self.check(r1.right,r2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root,root)