# Problem Id:  145
# Problem Name:  Binary Tree Postorder Traversal, 二叉树的后序遍历
# Problem Url:  https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(rt):
            if not rt:
                pass
            else:
                dfs(rt.left)
                dfs(rt.right)
                res.append(rt.val)
        dfs(root)
        return res
