# Problem Id:  94
# Problem Name:  Binary Tree Inorder Traversal, 二叉树的中序遍历
# Problem Url:  https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        save = []
        def dfs(root):
            if not root:
                pass
            else:
                dfs(root.left)
                save.append(root.val)
                dfs(root.right)
        dfs(root)
        return save