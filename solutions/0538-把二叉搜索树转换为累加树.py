# Problem Id:  538
# Problem Name:  Convert BST to Greater Tree, 把二叉搜索树转换为累加树
# Problem Url:  https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def at(self, root: TreeNode) -> TreeNode:
        if not root:
            return 0
        else:
            return root.val + self.at(root.left) + self.at(root.right)
    
    def addt(self, root: TreeNode, vl) -> TreeNode:
        if not root:
            return None
        else:
            root.val += vl
            root.left = self.addt(root.left, vl)
            root.right = self.addt(root.right, vl)
            return root

    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        else:
            root.left = self.convertBST(root.left)
            s = self.at(root.right)
            root.left = self.addt(root.left , s+root.val)
            root.val += s
            root.right = self.convertBST(root.right)
            return root
        

