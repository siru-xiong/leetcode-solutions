# Problem Id:  144
# Problem Name:  Binary Tree Preorder Traversal, 二叉树的前序遍历
# Problem Url:  https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(r):
            if not r:
                pass
            else:
                res.append(r.val)
                dfs(r.left)
                dfs(r.right)
        dfs(root)
        return res