# Problem Id:  257
# Problem Name:  Binary Tree Paths, 二叉树的所有路径
# Problem Url:  https://leetcode-cn.com/problems/binary-tree-paths/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        elif not root.left and not root.right:
            return [str(root.val)]
        else:
            l = self.binaryTreePaths(root.left)
            r = self.binaryTreePaths(root.right)
            l = [str(root.val)+'->'+i for i in l]
            r = [str(root.val)+'->'+i for i in r]
            return l+r