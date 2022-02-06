# Problem Id:  剑指 Offer 68 - II
# Problem Name:  二叉树的最近公共祖先 LCOF, 二叉树的最近公共祖先
# Problem Url:  https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return -1
        elif root.val in (p.val,q.val):
            return root
        else:
            l = self.lowestCommonAncestor(root.left,p,q)
            r = self.lowestCommonAncestor(root.right,p,q)
            if l != -1 and r == -1:
                return l
            elif r != -1 and l == -1:
                return r
            elif l == -1 and r == -1:
                return -1
            else:
                return root