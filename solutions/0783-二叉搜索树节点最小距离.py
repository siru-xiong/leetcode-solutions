# Problem Id:  783
# Problem Name:  Minimum Distance Between BST Nodes, 二叉搜索树节点最小距离
# Problem Url:  https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        vals = []
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        vals.sort()
        return min(vals[i+1] - vals[i]
                   for i in range(len(vals) - 1))
