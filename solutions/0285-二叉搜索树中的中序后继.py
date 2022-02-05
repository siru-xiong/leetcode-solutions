# Problem Id:  285
# Problem Name:  Inorder Successor in BST, 二叉搜索树中的中序后继
# Problem Url:  https://leetcode-cn.com/problems/inorder-successor-in-bst/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        elif root.val == p.val:
            if not root.right:
                return None
            else:
                q = root.right
                while q.left:
                    q = q.left
                return q
        elif root.val < p.val:
            return self.inorderSuccessor(root.right,p)
        else:
            t = self.inorderSuccessor(root.left,p)
            if t:
                return t
            else:
                return root
