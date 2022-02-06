# Problem Id:  剑指 Offer II 052
# Problem Name:  展平二叉搜索树, 展平二叉搜索树
# Problem Url:  https://leetcode-cn.com/problems/NYBBNL/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        elif not root.left and not root.right:
            return TreeNode(root.val)
        else:
            if root.left:
                res = self.increasingBST(root.left)
                r = res
                while r.right:
                    r = r.right
                r.right = TreeNode(root.val)
                r = r.right
                r.right = self.increasingBST(root.right)
                return res
            else:
                return TreeNode(val=root.val,right=self.increasingBST(root.right))
            return res
