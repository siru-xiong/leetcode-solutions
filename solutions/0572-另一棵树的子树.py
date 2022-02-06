# Problem Id:  572
# Problem Name:  Subtree of Another Tree, 另一棵树的子树
# Problem Url:  https://leetcode-cn.com/problems/subtree-of-another-tree/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def istree(self, s: TreeNode, t:TreeNode) -> bool:
        if not s and not t:
            return True
        elif not s and t or not t and s:
            return False
        else:
            return s.val == t.val and self.istree(s.left,t.left) and self.istree(s.right,t.right)
            
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        else:
            return self.istree(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)