# Problem Id:  701
# Problem Name:  Insert into a Binary Search Tree, 二叉搜索树中的插入操作
# Problem Url:  https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right,val)
            return root
        else:
            root.left = self.insertIntoBST(root.left,val)
            return root