# Problem Id:  617
# Problem Name:  Merge Two Binary Trees, 合并二叉树
# Problem Url:  https://leetcode-cn.com/problems/merge-two-binary-trees/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        elif not t1:
            return t2
        elif not t2:
            return t1
        else:
            return TreeNode(val=t1.val+t2.val,left=self.mergeTrees(t1.left,t2.left),right=self.mergeTrees(t1.right,t2.right))