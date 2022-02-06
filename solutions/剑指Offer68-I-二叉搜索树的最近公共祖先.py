# Problem Id:  剑指 Offer 68 - I
# Problem Name:  二叉搜索树的最近公共祖先 LCOF, 二叉搜索树的最近公共祖先
# Problem Url:  https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val in (p.val,q.val):
            return root
        else:
            if max(p.val,q.val) > root.val and min(p.val,q.val) < root.val:
                return root
            elif max(p.val,q.val) < root.val:
                return self.lowestCommonAncestor(root.left,p,q)
            else:
                return self.lowestCommonAncestor(root.right,p,q)