# Problem Id:  563
# Problem Name:  Binary Tree Tilt, 二叉树的坡度
# Problem Url:  https://leetcode-cn.com/problems/binary-tree-tilt/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tsum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return root.val+self.tsum(root.left)+self.tsum(root.right)

    def findTilt(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return abs(self.tsum(root.left)-self.tsum(root.right))+self.findTilt(root.left)+self.findTilt(root.right)