# Problem Id:  199
# Problem Name:  Binary Tree Right Side View, 二叉树的右视图
# Problem Url:  https://leetcode-cn.com/problems/binary-tree-right-side-view/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            res = [root.val]
            left = self.rightSideView(root.left)
            right = self.rightSideView(root.right)
            if len(right) >= len(left):
                res = res + right
            else:
                left[:len(right)] = right[:]
                res = res + left
            return res