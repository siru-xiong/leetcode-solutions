# Problem Id:  235
# Problem Name:  Lowest Common Ancestor of a Binary Search Tree, 二叉搜索树的最近公共祖先
# Problem Url:  https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Problem Level:  Easy
 
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