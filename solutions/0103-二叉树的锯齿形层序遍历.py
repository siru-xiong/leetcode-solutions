# Problem Id:  103
# Problem Name:  Binary Tree Zigzag Level Order Traversal, 二叉树的锯齿形层序遍历
# Problem Url:  https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# i = 0 means left
class Solution:
    def zigzagLevelOrder(self, root: TreeNode, i = 1) -> List[List[int]]:
        res = []
        def dfs(root,i,j):
            if not root:
                return
            while len(res) < i:
                res.append([])
            left = dfs(root.left,i+1,1-j)
            right = dfs(root.right,i+1,1-j)
            if j == 0:
                res[i-1] = res[i-1] + [root.val]
            else:
                res[i-1] = [root.val] + res[i-1]
        dfs(root,1,0)
        return res