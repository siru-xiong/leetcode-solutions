# Problem Id:  450
# Problem Name:  Delete Node in a BST, 删除二叉搜索树中的节点
# Problem Url:  https://leetcode-cn.com/problems/delete-node-in-a-bst/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def fl(self,root: TreeNode) -> TreeNode:
        if not root.left:
            return [root.val,root.right]
        else:
            t = self.fl(root.left)
            root.left = t[1]
            return [t[0],root]

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
            return root
        else:
            if root.right:
                t = self.fl(root.right)
                r = TreeNode(t[0],left = root.left,right = t[1])
                return r
            elif root.left:
                t = self.fl(root.left)
                r = TreeNode(t[0],left = None,right = t[1])
                return r
            else:
                return None