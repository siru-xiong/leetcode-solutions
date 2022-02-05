# Problem Id:  124
# Problem Name:  Binary Tree Maximum Path Sum, 二叉树中的最大路径和
# Problem Url:  https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
# Problem Level:  Hard
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxpath(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return root.val
        else:
            if not root.left:
                return root.val + max(self.maxpath(root.right),0)
            elif not root.right:
                return root.val + max(self.maxpath(root.left),0)
            else:
                return root.val + max(self.maxpath(root.left),self.maxpath(root.right),0)

    def maxPathSum(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return root.val
        else:
            if root.left:
                s1 = self.maxPathSum(root.left)
                if root.right:
                    s1 = max(s1,self.maxPathSum(root.right))
            else:
                s1 = self.maxPathSum(root.right)
            s2 = root.val
            if root.left:
                t = self.maxpath(root.left)
                if t > 0:
                    s2 += t
            if root.right:
                t = self.maxpath(root.right)
                if t > 0:
                    s2 += t
            return max(s1,s2)