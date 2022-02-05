# Problem Id:  101
# Problem Name:  Symmetric Tree, 对称二叉树
# Problem Url:  https://leetcode-cn.com/problems/symmetric-tree/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def t(self, root1,root2):
        if not root1 and not root2:
            return True
        elif not root1 and root2 or not root2 and root1:
            return False
        if root1.val != root2.val:
            return False
        else:
            return self.t(root1.left,root2.right) and self.t(root1.right,root2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.t(root,root)
        