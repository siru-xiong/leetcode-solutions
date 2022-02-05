# Problem Id:  105
# Problem Name:  Construct Binary Tree from Preorder and Inorder Traversal, 从前序与中序遍历序列构造二叉树
# Problem Url:  https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 and len(inorder) == 0:
            return None
        else:
            index = inorder.index(preorder[0])
            res = TreeNode(val=preorder[0])
            res.left = self.buildTree(preorder[1:(1+index)],inorder[:index])
            res.right = self.buildTree(preorder[(1+index):],inorder[(index+1):])
            return res