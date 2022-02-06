# Problem Id:  剑指 Offer 54
# Problem Name:  二叉搜索树的第k大节点  LCOF, 二叉搜索树的第k大节点
# Problem Url:  https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def ct(self, root: TreeNode):
        if not root:
            return 0
        else:
            return 1 + self.ct(root.left) + self.ct(root.right)

    def kthLargest(self, root: TreeNode, k: int) -> int:
        if k == -1:
            return root.val
        else:
            l = self.ct(root.left)
            r = self.ct(root.right)
            if k == r + 1:
                return root.val
            elif k <= r:
                return self.kthLargest(root.right,k)
            else:
                return self.kthLargest(root.left, k - r - 1)

