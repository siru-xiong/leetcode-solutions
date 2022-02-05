# Problem Id:  114
# Problem Name:  Flatten Binary Tree to Linked List, 二叉树展开为链表
# Problem Url:  https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                pass
            else:
                dfs(root.left)
                dfs(root.right)
                a = root
                while a.left:
                    a = a.left
                a.left = root.right
                root.right = None
        dfs(root)
        a = root
        while a:
            a.right , a.left = a.left , None
            a = a.right