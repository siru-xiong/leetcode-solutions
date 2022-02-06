# Problem Id:  230
# Problem Name:  Kth Smallest Element in a BST, 二叉搜索树中第K小的元素
# Problem Url:  https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def cc(self, root:TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + self.cc(root.left) + self.cc(root.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        x = self.cc(root.left)
        if k == x + 1:
            return root.val
        elif k < x + 1:
            return self.kthSmallest(root.left,k)
        else:
            return self.kthSmallest(root.right,k-x-1)