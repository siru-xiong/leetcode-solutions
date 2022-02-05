# Problem Id:  938
# Problem Name:  Range Sum of BST, 二叉搜索树的范围和
# Problem Url:  https://leetcode-cn.com/problems/range-sum-of-bst/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sv = []
        def ct(node):
            if node:
                if node.val >= low and node.val <= high:
                    sv.append(node.val)
                ct(node.left)
                ct(node.right)
        ct(root)
        return sum(sv)