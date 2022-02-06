# Problem Id:  106
# Problem Name:  Construct Binary Tree from Inorder and Postorder Traversal, 从中序与后序遍历序列构造二叉树
# Problem Url:  https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0 and len(postorder) == 0:
            return None
        if len(inorder) == 1 and len(postorder) == 1:
            return TreeNode(inorder[0])
        else:
            root = postorder[-1]
            for i in range(len(inorder)):
                if inorder[i] == root:
                    index = i
            leftinorder = inorder[:index]
            rightinorder = inorder[(index+1):]
            ln = len(leftinorder)
            leftpostorder = postorder[:ln]
            rightpostorder = postorder[ln:(-1)]
            return TreeNode(val= root,left= self.buildTree(leftinorder,leftpostorder),right = self.buildTree(rightinorder,rightpostorder))